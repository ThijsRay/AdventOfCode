import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Scanner;

public class Day16 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new BufferedReader(new FileReader("/home/thijs/Projects/AdventOfCode/day16/input2")));

        int[] registers = {0, 0, 0, 0};

        while (sc.hasNextLine()) {
            int opcode = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            sc.nextLine();

            switch (opcode) {
                case 0:
                    mulr(registers, a, b, c);
                    break;
                case 1:
                    addr(registers, a, b, c);
                    break;
                case 2:
                    banr(registers, a, b, c);
                    break;
                case 3:
                    eqir(registers, a, b, c);
                    break;
                case 4:
                    muli(registers, a, b, c);
                    break;
                case 5:
                    setr(registers, a, c);
                    break;
                case 6:
                    eqri(registers, a, b, c);
                    break;
                case 7:
                    gtri(registers, a, b, c);
                    break;
                case 8:
                    eqrr(registers, a, b, c);
                    break;
                case 9:
                    addi(registers, a, b, c);
                    break;
                case 10:
                    gtir(registers, a, b, c);
                    break;
                case 11:
                    gtrr(registers, a, b, c);
                    break;
                case 12:
                    borr(registers, a, b, c);
                    break;
                case 13:
                    bani(registers, a, b, c);
                    break;
                case 14:
                    seti(registers, a, c);
                    break;
                case 15:
                    bori(registers, a, b, c);
                    break;
                default:
                    throw new RuntimeException("Unknown opcode");
            }
            StringBuilder sb = new StringBuilder();
            sb.append("[");
            for (int reg : registers) {
                sb.append(reg);
                sb.append(", ");
            }
            sb.delete(sb.length()-2, sb.length());
            sb.append("]");
            System.out.println(sb);

        }


        sc.close();
    }

    public static boolean equals(int[] a, int[] b) {
        if (a.length != b.length) {
            return false;
        }
        for(int i  = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }

    public static int[] addr(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] + registers[b];
        return registers;
    }

    public static int[] addi(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] + b;
        return registers;
    }

    public static int[] mulr(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] * registers[b];
        return registers;
    }

    public static int[] muli(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] * b;
        return registers;
    }

    public static int[] banr(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] & registers[b];
        return registers;
    }

    public static int[] bani(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] & b;
        return registers;
    }

    public static int[] borr(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] | registers[b];
        return registers;
    }

    public static int[] bori(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] | b;
        return registers;
    }

    public static int[] setr(int[] registers, int a, int c) {
        registers[c] = registers[a];
        return registers;
    }

    public static int[] seti(int[] registers, int a, int c) {
        registers[c] = a;
        return registers;
    }

    public static int[] gtir(int[] registers, int a, int b, int c) {
        registers[c] = a > registers[b] ? 1 : 0;
        return registers;
    }

    public static int[] gtri(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] > b ? 1 : 0;
        return registers;
    }

    public static int[] gtrr(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] > registers[b] ? 1 : 0;
        return registers;
    }

    public static int[] eqir(int[] registers, int a, int b, int c) {
        registers[c] = a == registers[b] ? 1 : 0;
        return registers;
    }

    public static int[] eqri(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] == b ? 1 : 0;
        return registers;
    }

    public static int[] eqrr(int[] registers, int a, int b, int c) {
        registers[c] = registers[a] == registers[b] ? 1 : 0;
        return registers;
    }


}
