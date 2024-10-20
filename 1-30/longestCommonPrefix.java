// leetcode 14

import java.util.*;

public class longestCommonPrefix {

    public static String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String minStr = Arrays.stream(strs).min(Comparator.comparingInt(String::length)).orElse("");

        for (int i = 0; i < minStr.length(); i++) {
            for (String str : strs) {
                if (str.charAt(i) != minStr.charAt(i)) {
                    return minStr.substring(0, i);
                }
            }
        }

        return minStr;
    }

    public static void main(String[] args) {
        String[] strs = {"flow", "flowers", "fled"};
        System.out.println(longestCommonPrefix(strs));
    }
}