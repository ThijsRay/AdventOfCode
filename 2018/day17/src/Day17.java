import java.io.FileNotFoundException;

public class Day17 {

    public static void main(String[] args) throws FileNotFoundException {
        Grid grid = new Grid("/home/thijs/Projects/AdventOfCode/day17/input");
        Coordinate start = new Coordinate(500, 0);
        grid.addParticle(start);

        int amount = 0;

        for (int y = 0; y < grid.GRID_SIZE_Y; y++) {
            for (int x = 0; x < grid.GRID_SIZE_X; x++) {
                GridType element = grid.grid[y][x];
                if (element == GridType.WATER_STILL) {
                    amount++;
                }
            }
        }

        System.out.println(grid);
        System.out.println(amount);
    }

}
