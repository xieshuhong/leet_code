
import java.util.*;

public class groupAnagram2 {
    public static List<List<String>> groupAnagram(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for (String s: strs) {
            int[] zeros = new int[26];
            for (char c: s.toCharArray()) {
                zeros[c - 'a'] ++;
            }
            System.out.println("zeros" + zeros);
            String key = Arrays.toString(zeros);
            
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }

        return new ArrayList<>(res.values());
    }

    public static void main(String[] args) {
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> group_anagram = groupAnagram(strs);

        System.out.println(group_anagram);
    }
}
