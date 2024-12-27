public class maxSubArray {
    public static int maxSubArr(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        int currentValue = 0;
        for (int num: nums) {
            currentValue += num;
            maxSum = Math.max(maxSum, currentValue);
            if (currentValue < 0) {
                currentValue = 0;
            }
        }
        return maxSum;
    }


    public static void main(String[] args) {
        int[] nums ={-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArr(nums));
    }
 
}
