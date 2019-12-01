import java.io.FileNotFoundException;

public class Day18 {
    public static void main(String[] args) throws FileNotFoundException {
        Grid grid = Grid.readGrid("/home/thijs/Projects/AdventOfCode/day18/example_input");
        System.out.println(grid);
        for (int i = 0; i < 1; i++) {
            grid.minutePasses();
            System.out.println(grid);
        }

        int lumber = 0;
        int wooded = 0;

        for (char c : grid.toString().toCharArray()) {
            if (c == '#') {
                lumber += 1;
            }
            if (c == '|') {
                wooded += 1;
            }
        }

        System.out.println(grid);
        System.out.println(lumber * wooded);
    }
}
