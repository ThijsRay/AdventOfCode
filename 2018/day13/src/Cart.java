public class Cart {
    public Coordinate coordinate;
    public Direction direction;
    private int intersectionCount = 0;

    public Cart(Direction direction, Coordinate coordinate) {
        this.coordinate = coordinate;
        this.direction = direction;
    }

    public int getIntersectionCount() {
        return intersectionCount;
    }

    public void addIntersection() {
        if (intersectionCount >= 3) {
            intersectionCount = 1;
        } else {
            intersectionCount++;
        }
    }

    @Override
    public String toString() {
        switch (direction) {
            case NORTH:
                return "^";
            case EAST:
                return ">";
            case SOUTH:
                return "v";
            case WEST:
                return "<";
        }
        return " ";
    }
}
