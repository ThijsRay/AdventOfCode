import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.*;

public class Day5 {
    public static void main(String[] args) throws FileNotFoundException, InterruptedException {
        FileReader fileReader = new FileReader("/home/thijs/Projects/AdventOfCode/day5/input");
        Scanner sc = new Scanner(new BufferedReader(fileReader));

        String line = sc.nextLine();
        sc.close();

        List<String> characters = new ArrayList<>();

        for (char c : line.toCharArray()) {
            characters.add(String.valueOf(c));
        }

        LinkedList<String> result = fuseProcess(characters);

        sizeOfRemoved("A", result);
        sizeOfRemoved("B", result);
        sizeOfRemoved("C", result);
        sizeOfRemoved("D", result);
        sizeOfRemoved("E", result);
        sizeOfRemoved("F", result);
        sizeOfRemoved("G", result);
        sizeOfRemoved("H", result);
        sizeOfRemoved("I", result);
        sizeOfRemoved("J", result);
        sizeOfRemoved("K", result);
        sizeOfRemoved("L", result);
        sizeOfRemoved("M", result);
        sizeOfRemoved("N", result);
        sizeOfRemoved("O", result);
        sizeOfRemoved("P", result);
        sizeOfRemoved("Q", result);
        sizeOfRemoved("R", result);
        sizeOfRemoved("S", result);
        sizeOfRemoved("T", result);
        sizeOfRemoved("U", result);
        sizeOfRemoved("V", result);
        sizeOfRemoved("W", result);
        sizeOfRemoved("X", result);
        sizeOfRemoved("Y", result);
        sizeOfRemoved("Z", result);

    }

    private static int sizeOfRemoved(String removedChar, LinkedList<String> calculated) {
        List<String> characters = new ArrayList<>();

        for (String c : calculated) {
            if (!c.equals(removedChar.toUpperCase()) && !c.equals(removedChar.toLowerCase())) {
                characters.add(c);
            }
        }

        System.out.println(removedChar + " - " + fuseProcess(characters).size());
        return 0;
    }

    private static LinkedList<String> fuseProcess(List<String> characters) {
        LinkedList<String> result = new LinkedList<>();

        for (String character : characters) {
            if (areOppositeCase(result.peekLast(), character)) {
                result.removeLast();
            } else {
                result.addLast(character);
            }
        }

        return result;

    }

    private static boolean areOppositeCase(String a, String b) {
        if (a == null || b == null) {
            return false;
        }
        return a.toLowerCase().equals(b.toLowerCase()) && !a.equals(b);
    }
}
