# Game of Life
# This version by Roland Waddilove
# Original idea: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Use it, copy it, change it.

# import os
import turtle
import time

# Try with/without wraparound
# life = [
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,1,1,1,0,0,0],
#     [0,0,0,1,0,1,0,0,0],
#     [0,0,0,1,1,1,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0]
# ]

# You can make the board any size
# and change the start pattern...
life = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


def show_life_turtle():
    for r in range(rows):
        for c in range(cols):
            x = r * 30 - 220    # screen = 800 x 600
            y = c * 30 - 200    # centre drawing
            turtle.teleport(x, y)
            if life[r][c]:
                turtle.dot(25, 'red')
            else:
                turtle.dot(25, 'white')


def show_life():    # change to print empty space if you want
    for r in range(rows):
        for c in range(cols):
            print("0 ", end="") if life[r][c] else print(". ", end="")
        print()


# this assumes nothing beyond the border edges
def count_neighbours(row, col):
    n = 0
    for r in range(row-1, row+2):
        if r < 0 or r == rows: continue         # don't count if off board
        for c in range(col-1, col+2):
            if c < 0 or c == cols: continue     # don't count if off board
            n = n + life[r][c]
    return n - life[row][col]               # don't count the cell itself


# Alternative: wrap around top/bottom and right/left
def count_neighbours_wrap(row, col):
    n = 0
    for i in range(row-1, row+2):
        r = i
        if r == rows: r = 0     # last row wraparound
        if r < 0: r = rows-1    # 1st row wraparound
        for j in range(col-1, col+2):
            c = j
            if c < 0: c = cols-1    # 1st col wraparound
            if c == cols: c = 0     # last col wraparound
            n = n + life[r][c]

    return n - life[row][col]   # don't count the cell itself


def new_generation():
    # calculate next generation in life2
    for r in range(rows):
        for c in range(cols):
            if wraparound:
                n = count_neighbours_wrap(r, c)
            else:
                n = count_neighbours(r, c)
            if n < 2 or n > 3: life2[r][c] = 0   # <2 or >3 neighbours die under/over population
            if n == 3: life2[r][c] = 1       # cell born if empty and 3 neighbours
            if n == 2: life2[r][c] = life[r][c]       # no change

    # copy next gen to current gen
    for i in range(len(life)):
        life[i] = life2[i].copy()


def mouseclick(x, y) -> None:   # wait for a mouseclick
    global waitclick
    waitclick = False           # stop waiting for a click
    

# ================ MAIN =================
# os.system('cls') if os.name == 'nt' else os.system('clear')
rows = len(life)
cols = len(life[0])
life2 = [life[i].copy() for i in range(len(life))]  # 2nd board used when calculating next generation

turtle.setup(810, 650)      # window size
turtle.Screen().screensize(800, 600)    # canvas size = 800 x 600
turtle.speed(0)
turtle.hideturtle()
turtle.Screen().title("John Conway's Game of Life")
turtle.teleport(-250, 150)
turtle.write("John Conway's Game of Life", font=("Verdana", 25, "bold"))
turtle.teleport(-250, 80)
turtle.write("Cells with < 2 neighbours die (starvation)", font=("Verdana", 15, "normal"))
turtle.teleport(-250, 40)
turtle.write("Cells with > 3 neighbours die (overcrowding)", font=("Verdana", 15, "normal"))
turtle.teleport(-250, 0)
turtle.write("Cells with 2 or 3 neighbours live", font=("Verdana", 15, "normal"))
turtle.teleport(-250, -40)
turtle.write("Cells born in a space with 3 neighbours", font=("Verdana", 15, "normal"))
turtle.teleport(-250, -100)
turtle.write("Click to continue", font=("Verdana", 12, "italic"))

turtle.Screen().onclick(mouseclick)  # wait for a mouse click
turtle.Screen().listen()
waitclick = True
while waitclick:
    turtle.Screen().update()

wraparound = (turtle.textinput("Turtle Life:", "Enter = normal, w = wraparound: ") == "w")
turtle.Screen().clearscreen()
turtle.Screen().bgcolor('#404040')
turtle.penup()
turtle.hideturtle()
turtle.tracer(0)
done = False
generation = 0
while not done:
    generation += 1
    show_life_turtle()
    new_generation()
    turtle.Screen().update()
    time.sleep(0.5)         # time delay between generations
