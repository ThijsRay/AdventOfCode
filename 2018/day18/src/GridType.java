import java.util.ArrayList;
import java.util.EnumMap;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public enum GridType {
    OPEN_GROUND('.'),
    TREES('|'),
    LUMBERYARD('#'),
    NULL(' ');

    private char c;

    GridType(char c) {
        this.c = c;
    }

    @Override
    public String toString() {
        return String.valueOf(this.c);
    }

    public static GridType get(char type) {
        switch (type) {
            case '.':
                return OPEN_GROUND;
            case '|':
                return TREES;
            case '#':
                return LUMBERYARD;
            default:
                return NULL;
        }
    }

    public GridType newType(HashMap<GridType, Integer> count) {
        switch(this) {
            case OPEN_GROUND:
                if (count.get(TREES) >= 3) {
                    return TREES;
                } else {
                    return OPEN_GROUND;
                }
            case TREES:
                if (count.get(LUMBERYARD) >= 3) {
                    return LUMBERYARD;
                } else {
                    return TREES;
                }
            case LUMBERYARD:
                if (count.get(LUMBERYARD) >= 1 && count.get(TREES) >= 1) {
                    return LUMBERYARD;
                } else {
                    return OPEN_GROUND;
                }
        }
        return NULL;
    }

}


