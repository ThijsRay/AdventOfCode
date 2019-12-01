import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.*;

public class Grid {

    private static final int SIZE = 10;

    public char[][] previousGrid;
    public char[][] grid;

    private Grid(char[][] grid) {
        this.grid = grid;
        this.previousGrid = grid.clone();
    }

    public static Grid readGrid(String fileName) throws FileNotFoundException {
        Scanner sc = new Scanner(new BufferedReader(new FileReader(fileName)));

        Grid grid = new Grid(new char[SIZE][SIZE]);

        int y = 0;
        while (sc.hasNext()) {
            String next = sc.next();
            for (int x = 0; x < next.length(); x++) {
                grid.set(GridType.get(next.charAt(x)), x, y);
            }
            y++;
        }

        return grid;
    }

    public void minutePasses() {
        for (int y = 0; y < SIZE; y++) {
            for (int x = 0; x < SIZE; x++) {
                set(getPrevious(x, y).newType(getAdjecentTiles(x, y)), x, y);
            }
        }

        previousGrid = grid.clone();
    }

    public void set(GridType gridType, int x, int y) {
        grid[y][x] = gridType.toString().charAt(0);
    }

    public GridType getPrevious(int x, int y) {
        return (isValidCoordinate(x, y)) ? GridType.get(previousGrid[y][x]) : GridType.NULL;
    }

    public HashMap<GridType, Integer> getAdjecentTiles(int x, int y) {
        ArrayList<GridType> adjecentTiles = new ArrayList<>(8);

        int tree = 0;
        int open = 0;
        int lumb = 0;

        adjecentTiles.add(getPrevious(x - 1, y - 1));
        adjecentTiles.add(getPrevious(x, y - 1));
        adjecentTiles.add(getPrevious(x + 1, y - 1));
        adjecentTiles.add(getPrevious(x - 1, y));
        adjecentTiles.add(getPrevious(x + 1, y));
        adjecentTiles.add(getPrevious(x - 1, y + 1));
        adjecentTiles.add(getPrevious(x, y + 1));
        adjecentTiles.add(getPrevious(x + 1, y + 1));

        for (GridType g : adjecentTiles) {
            switch (g) {
                case OPEN_GROUND:
                    open += 1;
                    break;
                case LUMBERYARD:
                    lumb += 1;
                    break;
                case TREES:
                    tree += 1;
                    break;
            }
        }

        System.out.println("T:" + tree + " O:" + open + " L:" + lumb);

        HashMap<GridType, Integer> map = new HashMap<GridType, Integer>();
        map.put(GridType.LUMBERYARD, Integer.valueOf(lumb));
        map.put(GridType.OPEN_GROUND, Integer.valueOf(open));
        map.put(GridType.TREES, Integer.valueOf(tree));

        return map;
    }

    private boolean isValidCoordinate(int x, int y) {
        if (x < 0 || x >= SIZE || y < 0 || y >= SIZE) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (char[] y : grid) {
           for (char x : y) {
               sb.append(x);
           }
           sb.append("\n");
        }
        return sb.toString();
    }

}
