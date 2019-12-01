import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Day13 {
    public static void main(String[] args) throws FileNotFoundException, InterruptedException {
        Field field = Field.readField("/home/thijs/Projects/AdventOfCode/day13/input");
        System.out.println("");
        while (true) {
//            System.out.println(field);
//            Thread.sleep(100);
            field.carts.sort((cart, t1) -> {
                if (cart.coordinate.y < t1.coordinate.y) {
                    return -1;
                }
                if (cart.coordinate.y > t1.coordinate.y) {
                    return 1;
                }
                return 0;
            });

            field.carts.sort((cart, t1) -> {
                if (cart.coordinate.x < t1.coordinate.x) {
                    return -1;
                }
                if (cart.coordinate.x > t1.coordinate.x) {
                    return 1;
                }
                return 0;
            });

            for (Cart cart : new ArrayList<>(field.carts)) {
                field.moveCart(cart);
                System.out.println(field.carts.size());
            }

            if (field.carts.size() == 1) {
                Cart cart = field.carts.get(0);
                throw new RuntimeException("Last cart is at x=" + cart.coordinate.x + " and y=" + cart.coordinate.y);
            }

        }

    }
}
