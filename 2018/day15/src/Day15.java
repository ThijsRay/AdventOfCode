import java.util.ArrayList;
import java.util.List;

public class Day15 {

    public static void main(String[] args) {
        ArrayList<Integer> recipeList = new ArrayList<>();
//        recipeList.add(3);
//        recipeList.add(7);
        recipeList.add(6);
        recipeList.add(8);
        recipeList.add(1);
        recipeList.add(9);
        recipeList.add(0);
        recipeList.add(1);
        int initial_size = 681901;

        int elf1 = 0;
        int elf2 = 1;

        System.out.println(recipeList);
        for (int i = 0; i < 682000; i++) {
            recipeList.addAll(calculateNewRecipes(recipeList, elf1, elf2));
            elf1 = moveElf(recipeList, elf1);
            elf2 = moveElf(recipeList, elf2);
        }

        System.out.println(recipeList.subList(initial_size, initial_size+10).toString().replaceAll(", ", ""));
    }

    public static int moveElf(ArrayList<Integer> list, int pointer) {
        return (pointer + list.get(pointer) + 1) % list.size();
    }

    public static ArrayList<Integer> calculateNewRecipes(ArrayList<Integer> list, int index1, int index2) {
        int result1 = list.get(index1);
        int result2 = list.get(index2);

        ArrayList<Integer> returnValue = new ArrayList<>();

        String sumString = String.valueOf(result1 + result2);
        if (sumString.length() == 1) {
            returnValue.add(Integer.valueOf(sumString));
        } else if (sumString.length() == 2) {
            returnValue.add(Integer.valueOf(sumString.substring(0,1)));
            returnValue.add(Integer.valueOf(sumString.substring(1,2)));
        }

        return returnValue;
    }

}
