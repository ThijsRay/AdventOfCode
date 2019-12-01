public enum Direction {
    NORTH,
    EAST,
    SOUTH,
    WEST;

    public Direction add(int amount) {
        Direction direction = this;
        for (int i = 0; i < amount; i++) {
            direction = singleAdd(direction);
        }
        return direction;
    }

    private Direction singleAdd(Direction d) {
        switch (d) {
            case NORTH:
                return EAST;
            case EAST:
                return SOUTH;
            case SOUTH:
                return WEST;
            case WEST:
                return NORTH;
        }
        return d;
    }
}

