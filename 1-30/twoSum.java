import java.util.Map;
import java.util.HashMap;

public class twoSum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numberToIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int numNeeded = target - nums[i];
            
            System.out.println("numNeeded: " + numNeeded + " " + "numberToIndex.containsKey(numNeeded)" + " " + numberToIndex.containsKey(numNeeded));
            if (numberToIndex.containsKey(numNeeded)) {
                System.out.println("numberToIndex.get(numNeeded)" + numberToIndex.get(numNeeded));
                return new int[] {numberToIndex.get(numNeeded), i};
            }
            numberToIndex.put(nums[i], i);
        }

        return null;

    }


    public static void main(String[] args) {
        int[] nums = {8, 9, 6, 5, 7};
        int target = 12;

        int[] result = twoSum(nums, target);

       System.out.println("Indices: " + result[0] + ", " + result[1]);

    }
}