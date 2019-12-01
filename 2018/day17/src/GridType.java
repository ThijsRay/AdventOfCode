public enum GridType {
    SAND("."),
    CLAY("#"),
    WATER_SPRING("+"),
    WATER_FLOW("|"),
    WATER_STILL("~");

    private String notation;

    GridType(String notation) {
        this.notation = notation;
    }

    @Override
    public String toString() {
        return this.notation;
    }
}
