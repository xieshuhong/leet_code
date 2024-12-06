public class powOfN50 {

    public static double powOfN(double x, int n) {
        double result = helper(x, Math.abs(n));
        return n >= 0 ? result : 1 / result;
    }

    public static double helper(double x, int n) {
        if (x == 0 ) return 0;
        if (n == 0 ) return 1;
        double res = helper(x * x, n / 2);
        if (n % 2 != 0) return x * res;
        else return res;

    }

    public static void main(String[] args) {
        System.out.println(powOfN(5, 3));
    }
    
}
