import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class mergeIntervals56 {
    
    public static List<int[]> mergeInterval(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> results = new ArrayList<>();
        results.add(intervals[0]);

        for (int[] interval: intervals) {
            int[] lastInterval = results.get(results.size() - 1);
            int lastEnd = lastInterval[1];
            if (lastEnd >= interval[0]) {
                lastInterval[1] = Math.max(lastEnd, interval[1]);
            } else {
                results.add(interval);
            }
        }
        return results;
    }
    
    public static void main(String[] args) {
        int[][] intervals = {{2,6}, {1,3}, {15,18}, {8,10}};
        List<int[]> mergedIntervals = mergeInterval(intervals);
        
        for (int[] interval: mergedIntervals) {
            System.out.println(Arrays.toString(interval));
        }
    }

}
