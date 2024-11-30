

import java.util.*;
public class groupAnagram1 {

    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for (String s: strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            System.out.println("chars " + Arrays.toString(chars));
            String key = new String(chars);
            System.out.println("key " + key);

            res.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(res.values());
    }


    public static void main(String[] args) {
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> grouped_anagrams = groupAnagrams(strs);
        System.out.println(grouped_anagrams);
    }
    
}
