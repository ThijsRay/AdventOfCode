import java.util.ArrayList;

public class Claim {
    public int id;
    public int offsetTop;
    public int offsetLeft;
    public int width;
    public int height;
    public boolean overlaps = false;

    public Claim(int id, int offsetLeft, int offsetTop, int width, int height) {
        this.id = id;
        this.offsetLeft = offsetLeft;
        this.offsetTop = offsetTop;
        this.width = width;
        this.height = height;
    }

    public ArrayList<Coordinate> getAllCoordinates() {
        ArrayList<Coordinate> coordinates = new ArrayList<>(width * height);
        for (int y = offsetTop; y < (offsetTop + height); y++) {
            for (int x = offsetLeft; x < (offsetLeft + width); x++) {
                coordinates.add(new Coordinate(x, y));
            }
        }
        return coordinates;
    }

    @Override
    public String toString() {
        return "#" + id + " " + offsetLeft + "," + offsetTop + " " + width + "x" + height;
    }
}
