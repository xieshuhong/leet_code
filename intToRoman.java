public class intToRoman {
    public static String intToRoman(int num) {
        String[][] romanNumerals = {
            {"M", "1000"},
            {"CM", "900"},
            {"D", "500"},
            {"CD", "400"},
            {"C", "100"},
            {"XC", "90"},
            {"L", "50"},
            {"XL", "40"},
            {"X", "10"},
            {"IX", "9"},
            {"V", "5"},
            {"IV", "4"},
            {"I", "1"}
        };
        StringBuilder result = new StringBuilder();
        for (String[] pair: romanNumerals) {
            String symbol = pair[0];
            int value = Integer.parseInt(pair[1]);

            while (num >= value) {
                result.append(symbol);
                num -= value;
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(intToRoman(1994));
    }
}


















