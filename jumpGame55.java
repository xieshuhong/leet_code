public class jumpGame55 {
    public static boolean jumpGame(int[] nums) {
        int goal = nums.length - 1;
        for (int i = nums.length - 2; i >= 0; i --) {
            if (i + nums [i] >= goal) goal = i;
        }
        if (goal == 0) return true;
        else return false;
    }

    public static void main(String[] args) {
        int[] nums = {2,3,1,1,4};
        System.out.println(jumpGame(nums));
    }
}
