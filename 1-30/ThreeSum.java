import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        // Step 1: Sort the array to apply the two-pointer approach
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        
        // Step 2: Loop through the array to treat each number as the first element of a triplet
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate numbers for the first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // skip to the next iteration to avoid duplicates
            }

            int left = i + 1;
            int right = nums.length - 1;

            // Step 3: Two-pointer technique to find two other numbers
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    // Found a valid triplet
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // Move left pointer to avoid duplicate numbers
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    // Move right pointer to avoid duplicate numbers
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    // Move both pointers after recording the triplet
                    left++;
                    right--;
                } else if (sum < 0) {
                    // If sum is less than zero, move left to the right to increase the sum
                    left++;
                } else {
                    // If sum is greater than zero, move right to the left to decrease the sum
                    right--;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        ThreeSum solution = new ThreeSum();
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> triplets = solution.threeSum(nums);
        System.out.println(triplets); // Output: [[-1, -1, 2], [-1, 0, 1]]
    }
}