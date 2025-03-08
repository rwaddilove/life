// Game of Life
// This version by Roland Waddilove (https://github.com/rwaddilove/)
// Original idea: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
// Public domain. Use it, copy it, change it, laugh at the bad code!

import java.util.Scanner;

class Life {
    public static void Show(int[][] life) {
        // life visible area is inner area - there's a one cell border top/bottom/left/right
        for (int row = 1; row < (life.length-1); ++row) {           // ignore top/bottom rows
            for (int col = 1; col < (life[0].length-1); ++col) {    // ignore left/right columns
                if (life[row][col] == 0)
                    System.out.print(" . ");
                else
                    System.out.print(" 0 ");
            }
            System.out.println();
        }
    }

    public static void NewGeneration(int[][] life, int[][] life2) {   // build next gen in life2
        int count;
        for (int row = 1; row < (life.length - 1); ++row) {           // ignore top/bottom rows
            for (int col = 1; col < (life[0].length - 1); ++col) {    // ignore left/right columns
                count = life[row-1][col-1]+life[row-1][col]+life[row-1][col+1]+life[row][col-1]+life[row][col+1]+life[row+1][col-1]+life[row+1][col]+life[row+1][col+1];
                life2[row][col] = 0;        // assume starved or overcrowded- count<2 or count>3
                if (life[row][col] == 1)    // if there's a cell here
                    life2[row][col] = (count == 2 || count == 3) ? 1 : 0;   // 2 or 3 neighbours lives
                else
                    life2[row][col] = (count == 3) ? 1 : 0;     // new cell born if 3 neighbours
            }
        }
        for (int row = 0; row < (life.length); ++row) {           // copy life2 to life
            for (int col = 0; col < (life[0].length); ++col)
                life[row][col] = life2[row][col];
        }
    }

    public static void Wrap(int[][] life) {
        // use top/bottom/left/right edges for wrap, then use NewGeneration as usual
        for (int col = 0; col < life[0].length; ++col) {
            life[0][col] = life[life.length-2][col];    // copy visible bottom row to top
            life[life.length-1][col] = life[1][col];    // copy visible top row to bottom
        }
        for (int row = 0; row < life.length; ++row) {       // for each row in life
            life[row][0] = life[row][life[0].length-2];     // copy visible right edge to left edge
            life[row][life[0].length-1] = life[row][1];     // copy visible left edge to right edge
        }
    }
}

public class LifeGame {
    public static void main(String[] args) {
        // edit this, but don't use top/bottom/left/right edges, they're used with Wrap()
        int[][] life = {
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,1,1,1,0,0,0,0},
                {0,0,0,0,1,1,1,0,0,0,0},
                {0,0,0,0,1,1,1,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0}
        };

/*      // change the size + start pattern. Uncomment this, comment above
        int[][] life = {
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
        };
*/
        int[][] life2 = new int[life.length][life[0].length];  // used to calculate next generation
        int generation = 0;
        Scanner input = new Scanner(System.in);

        System.out.println("----------------------------");
        System.out.println(" John Conway's Game of Life");
        System.out.println("----------------------------");
        System.out.println("Cells with < 2 neighbours die (starves)");
        System.out.println("Cells with > 3 neighbours die (crowded)");
        System.out.println("Cells with 2 or 3 neighbours live");
        System.out.println("Cells born in a space with 3 neighbours\n");

        System.out.print("(N)ormal game or (W)rap-around? ");
        String wrap = input.nextLine().strip().toUpperCase();

        while (true) {
            Life.Show(life);
            if (wrap.startsWith("W")) Life.Wrap(life);
            Life.NewGeneration(life, life2);
            System.out.print("Generation "+(++generation) + ": Enter=Next or Q=Quit");
            if (!input.nextLine().isBlank()) break;     // enter anything to quit
        }

    }
}
