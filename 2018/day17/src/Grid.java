import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Grid {

    private int count = 0;
    public int GRID_SIZE_Y = 1972;
    public int GRID_SIZE_X = 195;
    public GridType[][] grid = new GridType[GRID_SIZE_Y][GRID_SIZE_X];

    public Grid(String fileName) throws FileNotFoundException {
        Scanner sc = new Scanner(new BufferedReader(new FileReader(fileName)));
        initWithSand();
        set(GridType.WATER_SPRING, new Coordinate(500, 0));
        while (sc.hasNextLine()) {
            ArrayList<Integer> x = new ArrayList<>();
            ArrayList<Integer> y = new ArrayList<>();

            String line = sc.nextLine();
            if (line.charAt(0) == 'x') {
                String[] lineArray = line.substring(2).split(", y=");
                x.add(Integer.valueOf(lineArray[0]));

                lineArray = lineArray[1].split("\\.\\.");
                for (int i = Integer.valueOf(lineArray[0]); i <= Integer.valueOf(lineArray[1]); i++) {
                    y.add(i);
                }
            } else if (line.charAt(0) == 'y') {
                String[] lineArray = line.substring(2).split(", x=");
                y.add(Integer.valueOf(lineArray[0]));

                lineArray = lineArray[1].split("\\.\\.");
                for (int i = Integer.valueOf(lineArray[0]); i <= Integer.valueOf(lineArray[1]); i++) {
                    x.add(i);
                }
            }

            for (int xCoordinate : x) {
                for (int yCoordinate : y) {
                    set(GridType.CLAY, new Coordinate(xCoordinate, yCoordinate));
                }
            }

        }
        sc.close();
    }

    public void addParticle(Coordinate coordinate) {
        if (get(coordinate.down()) == GridType.SAND) {
            set(GridType.WATER_FLOW, coordinate.down());
            addParticle(coordinate.down());
        }

        GridType down = get(coordinate.down());
        if (down == GridType.CLAY || down == GridType.WATER_STILL) {
            if (get(coordinate.right()) == GridType.SAND) {
                set(GridType.WATER_FLOW, coordinate.right());
                addParticle(coordinate.right());
            }

            if (get(coordinate.left()) == GridType.SAND) {
                set(GridType.WATER_FLOW, coordinate.left());
                addParticle(coordinate.left());
            }
        }

        if (hasBothWalls(coordinate)) {
            fillLevel(coordinate);
        }

    }

    public boolean hasBothWalls(Coordinate coordinate) {
        return hasWall(coordinate, 1) && hasWall(coordinate, -1);
    }

    public boolean hasWall(Coordinate coordinate, int offset) {
        int currentX = coordinate.x;
        while (true) {
            if (get(new Coordinate(currentX, coordinate.y)) == GridType.SAND) {
                return false;
            }
            if (get(new Coordinate(currentX, coordinate.y)) == GridType.CLAY) {
                return true;
            }
            currentX += offset;
        }
    }

    public void fillLevel(Coordinate coordinate) {
        fillSide(coordinate, 1);
        fillSide(coordinate, -1);
    }

    public void fillSide(Coordinate coordinate, int offset) {
        int currentX = coordinate.x;
        while (true) {
            if (get(new Coordinate(currentX, coordinate.y)) == GridType.CLAY) return;
            set(GridType.WATER_STILL, new Coordinate(currentX, coordinate.y));
            currentX += offset;
        }
    }

    public void set(GridType type, Coordinate coordinate) {
        grid[coordinate.y][coordinate.x-431] = type;
    }

    public GridType get(Coordinate coordinate) {
        try {
            return grid[coordinate.y][coordinate.x - 431];
        } catch (ArrayIndexOutOfBoundsException e) {

        }
        return null;
    }

    private void initWithSand() {
        for (int y = 0; y < GRID_SIZE_Y; y++) {
            for (int x = 0; x < GRID_SIZE_X; x++) {
                grid[y][x] = GridType.SAND;
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int y = 0; y < GRID_SIZE_Y; y++) {
            for (int x = 0; x < GRID_SIZE_X; x++) {
                sb.append(grid[y][x]);
            }
            sb.append("\n");
        }
        return sb.toString();
    }

}
