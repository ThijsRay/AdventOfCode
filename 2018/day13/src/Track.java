import java.util.Map;

public class Track {
    public TrackType trackType;
    public Coordinate coordinate;

    public Track[] neighbourTracks = new Track[4];

    public Track(TrackType trackType) {
        this.trackType = trackType;
    }

    @Override
    public String toString() {
        switch (trackType) {
            case BACKSLASH:
                return "\\";
            case SLASH:
                return "/";
            case HORIZONTAL:
                return "-";
            case VERTICAL:
                return "|";
            case INTERSECTION:
                return "+";
        }
        return " ";
    }
}
