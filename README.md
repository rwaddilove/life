Game of Life

John Conway's game of Life, a Python learning exercise by Roland Waddilove. Original idea: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

*Game of Life 8.py*: A text app that runs in the terminal window.

*Game of Life 10 GUI.py* Same code, but outputs to a graphical window using Python Turtle.

Bug: I don't know why, but if you click the window close button on the opening screen, the app gets stuck and the window won't close. (Force quit, or close VS Code.) Click the window close button when the life sim is running and the app closes OK. Am I doing something or is this a turtle bug?

I've seen people ask how to pause/stop Python turtle, such as to wait for user input. Here I use:

def mouseclick(x, y):   # wait for a mouseclick
    global waitclick
    waitclick = False   # stop waiting for a click
.
.
turtle.Screen().onclick(mouseclick)  # wait for a mouse click
turtle.Screen().listen()
waitclick = True
while waitclick:
    turtle.Screen().update()

Maybe it's this that is causing the problem. Click the screen and the app continues. Click the window close button and it hangs.
