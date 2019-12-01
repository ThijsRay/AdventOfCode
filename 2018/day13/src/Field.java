import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Field {
    private Track[][] tracks;
    public ArrayList<Cart> carts = new ArrayList<>();

    public Field(int maxX, int maxY) {
        tracks = new Track[maxY][maxX];
    }

    public Track getTrackAtCoordinate(Coordinate coordinate) {
        return tracks[coordinate.y][coordinate.x];
    }

    public boolean hasCartOnCoordinate(Coordinate coordinate) {
        for (Cart cart : carts) {
            if (cart.coordinate.x == coordinate.x && cart.coordinate.y == coordinate.y) {
                return true;
            }
        }
        return false;
    }

    public Cart getCartOnCoordinate(Coordinate coordinate) {
        for (Cart cart : carts) {
            if (cart.coordinate.x == coordinate.x && cart.coordinate.y == coordinate.y) {
                return cart;
            }
        }
        return null;
    }

    public Direction moveCart(Cart cart) {
        Coordinate coordinate = cart.coordinate;

        Direction direction = cart.direction;

        Coordinate newCoordinate = null;
        switch (direction) {
            case NORTH:
                newCoordinate = new Coordinate(coordinate.x, coordinate.y - 1);
                break;
            case EAST:
                newCoordinate = new Coordinate(coordinate.x + 1, coordinate. y);
                break;
            case SOUTH:
                newCoordinate = new Coordinate(coordinate.x, coordinate.y + 1);
                break;
            case WEST:
                newCoordinate = new Coordinate(coordinate.x - 1, coordinate.y);
                break;
        }
        Track newLocation = getTrackAtCoordinate(newCoordinate);
        if (hasCartOnCoordinate(newCoordinate)) {
            carts.remove(cart);
            carts.remove(getCartOnCoordinate(newCoordinate));
//            throw new RuntimeException("Crash on x=" + newCoordinate.x + "\ty=" + newCoordinate.y);
        }

        cart.coordinate = newCoordinate;

        Direction newDirection = direction;
        switch (newLocation.trackType) {
            case INTERSECTION:
                cart.addIntersection();
                switch (direction) {
                    case NORTH:
                        switch(cart.getIntersectionCount()) {
                            case 1:
                                newDirection = Direction.WEST;
                                break;
                            case 3:
                                newDirection = Direction.EAST;
                                break;
                        }
                        break;
                    case WEST:
                        switch(cart.getIntersectionCount()) {
                            case 1:
                                newDirection = Direction.SOUTH;
                                break;
                            case 3:
                                newDirection = Direction.NORTH;
                                break;
                        }
                        break;
                    case SOUTH:
                        switch(cart.getIntersectionCount()) {
                            case 1:
                                newDirection = Direction.EAST;
                                break;
                            case 3:
                                newDirection = Direction.WEST;
                                break;
                        }
                        break;
                    case EAST:
                        switch(cart.getIntersectionCount()) {
                            case 1:
                                newDirection = Direction.NORTH;
                                break;
                            case 3:
                                newDirection = Direction.SOUTH;
                                break;
                        }
                        break;
                }
                break;
            case SLASH:
                switch (direction) {
                    case NORTH:
                        newDirection = Direction.EAST;
                        break;
                    case EAST:
                        newDirection = Direction.NORTH;
                        break;
                    case WEST:
                        newDirection = Direction.SOUTH;
                        break;
                    case SOUTH:
                        newDirection = Direction.WEST;
                        break;
                }
                break;
            case BACKSLASH:
                switch (direction) {
                    case NORTH:
                        newDirection = Direction.WEST;
                        break;
                    case EAST:
                        newDirection = Direction.SOUTH;
                        break;
                    case WEST:
                        newDirection = Direction.NORTH;
                        break;
                    case SOUTH:
                        newDirection = Direction.EAST;
                        break;

                }
                break;

        }
        cart.direction = newDirection;
        return newDirection;
    }

    public static Field readField(String fileName) throws FileNotFoundException {
        FileReader fileReader = new FileReader(fileName);
        Scanner sc = new Scanner(new BufferedReader(fileReader));

        Field f = new Field(150, 150);

        int y = 0;
        while (sc.hasNextLine()) {
            int x = 0;
            String line = sc.nextLine();
            for (char c : line.toCharArray()) {
                Track track = null;
                Cart cart = null;
                switch (c) {
                    case ' ':
                        break;
                    case '|':
                        track = new Track(TrackType.VERTICAL);
                        break;
                    case '-':
                        track = new Track(TrackType.HORIZONTAL);
                        break;
                    case '/':
                        track = new Track(TrackType.SLASH);
                        break;
                    case '\\':
                        track = new Track(TrackType.BACKSLASH);
                        break;
                    case '+':
                        track = new Track(TrackType.INTERSECTION);
                        break;
                    case '>':
                        track = new Track(TrackType.HORIZONTAL);
                        cart = new Cart(Direction.EAST, new Coordinate(x, y));
                        break;
                    case '<':
                        track = new Track(TrackType.HORIZONTAL);
                        cart = new Cart(Direction.WEST, new Coordinate(x, y));
                        break;
                    case '^':
                        track = new Track(TrackType.VERTICAL);
                        cart = new Cart(Direction.NORTH, new Coordinate(x, y));
                        break;
                    case 'v':
                        track = new Track(TrackType.VERTICAL);
                        cart = new Cart(Direction.SOUTH, new Coordinate(x, y));
                        break;
                }
                f.tracks[y][x] = track;
                if (cart != null) {
                    f.carts.add(cart);
                }
                x++;

            }
            y++;
        }

        return f;
    }

    public void printCarts() {
        for (Cart cart : carts) {
            System.out.println(cart.toString());
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int y = 0; y < 150; y++) {
            for (int x = 0; x < 150; x++) {
                Track track = this.tracks[y][x];
                Cart cart = this.getCartOnCoordinate(new Coordinate(x, y));
                if (cart != null) {
                    sb.append(cart);
                } else if (track != null) {
                    sb.append(track.toString());
                } else {
                    sb.append(" ");
                }
            }
            sb.append("\n");
        }
        return sb.toString();
    }
}
