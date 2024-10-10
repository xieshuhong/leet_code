
public class waterContainerMaxArea {
    public static int maxArea(int[] heights) {
        int res = 0;
        int l = 0;
        int r = heights.length - 1;

        while (l < r) {
            int area = Math.min(heights[l], heights[r]) * (r - l);
            res = Math.max(res, area);

            if (heights[l] < heights[r]) l++;
            else r--;
        }
        return res;
    }

    public static void main(String[] args) {
        int[] heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(maxArea(heights));
    }


}