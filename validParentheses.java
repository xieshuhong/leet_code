
import java.util.HashMap;
import java.util.Stack;

public class validParentheses {
    public static boolean isValid(String s) {
        // Create a stack to keep track of opening brackets
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (mapping.containsKey(currentChar)) {
                char topElement = stack.isEmpty() ? '#' : stack.pop();
                if (topElement != mapping.get(currentChar)) {
                    return false;
                }
            } else {
                stack.push(currentChar);
            }
        } 
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s1 = "([{}])";
        System.out.println(isValid(s1));
        String s2 = "([)]";
        System.out.println(isValid(s2)); // Output: false
    }


}