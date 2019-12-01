import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Day3 {

    public static void main(String[] args) throws FileNotFoundException {
        FileReader fileReader = new FileReader("/home/thijs/Projects/AdventOfCode/day3/input");
        Scanner sc = new Scanner(new BufferedReader(fileReader));

        ArrayList<Claim> claims = new ArrayList<>(1500);

        int[][] sheet = new int[1000][1000];

        for (int i = 0; i < 1253; i++) {
            String line = sc.nextLine().replace('#', ' ').trim();
            String[] segments = line.split("[^0-9]+");
            claims.add(new Claim(
                    Integer.valueOf(segments[0]),
                    Integer.valueOf(segments[1]),
                    Integer.valueOf(segments[2]),
                    Integer.valueOf(segments[3]),
                    Integer.valueOf(segments[4])
            ));
        }


        for (Claim claim : claims) {
            for (Coordinate coordinate : claim.getAllCoordinates()) {
                sheet[coordinate.x][coordinate.y]++;
            }
        }

        for (Claim claim : claims) {
            for (Coordinate coordinate : claim.getAllCoordinates()) {
                if (sheet[coordinate.x][coordinate.y] >= 2) {
                    claim.overlaps = true;
                }
            }
        }

        for (Claim claim : claims) {
            if (!claim.overlaps) {
                System.out.println(claim.id);
            }
        }

//        int overlap = 0;
//        for (int x = 0; x < 1000; x++) {
//            for (int y = 0; y < 1000; y++) {
//                if (sheet[x][y] > 1) {
//                    overlap++;
//                }
//            }
//        }

//        System.out.println(overlap);
    }

}
