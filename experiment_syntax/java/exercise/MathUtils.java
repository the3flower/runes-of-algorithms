class MathUtils {
    private static int square(int x) {
        return x*x;
    }

    public static void printSquare(int x) {
        int result = square(x);
        System.out.print("Square of " + x);
        System.out.print(" is " + result);
    }

    public static void main(String[] args) {
        MathUtils.printSquare(5);
    }
}