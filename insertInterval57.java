import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class insertInterval57 {
    public static List<int[]> insertInterval(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        if (intervals.length == 0) {
            res.add(newInterval);
            return res;
        }

        for (int i = 0; i < intervals.length; i++) {
            if (newInterval[0] > intervals[i][1]){
                res.add(intervals[i]);
            } else if (newInterval[1] < intervals[i][0]) {
                res.add(newInterval);
                for (int j = i; j < intervals.length; j++) {
                    res.add(intervals[j]);
                }
                return res;
            } else {
                newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
                newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            }
        }
        res.add(newInterval);
        return res;
    }

    public static void main(String[] args) {
        int[][] intervals = {{1,2},{3,5},{6,7},{8,10},{12,16}};
        int[] newInterval = {4, 8};
        List<int[]> newIntervals =  insertInterval(intervals, newInterval);

        for (int[] interval: newIntervals) {
            System.out.println(Arrays.toString(interval));
        }


    }
    
}
