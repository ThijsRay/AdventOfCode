import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day4 {

    public static void main(String[] args) throws FileNotFoundException {
        FileReader fileReader = new FileReader("/home/thijs/Projects/AdventOfCode/day4/input");
        Scanner sc = new Scanner(new BufferedReader(fileReader));

        Map<Integer, Guard> map = new HashMap<>();

        int lastId;
        Guard lastGuard = new Guard(0);
        int lastSleepTime = 0;

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            if (line.contains("begins shift")) {
                lastId = Integer.valueOf(line.substring(26, line.length()).replace("begins shift", "").trim());
                lastGuard = map.getOrDefault(lastId, new Guard(lastId));
                map.putIfAbsent(lastId, lastGuard);
            } else if (line.contains("falls asleep")) {
                lastSleepTime = Integer.valueOf(line.substring(15, 17));
            } else if (line.contains("wakes up")) {
                int endTime = Integer.valueOf(line.substring(15, 17));
                for (int i = lastSleepTime; i < endTime; i++) {
                    lastGuard.sleepingTime[i]++;
                }
            }
        }

        for (Guard guard : map.values()) {
            System.out.println(guard);
        }

    }

}
