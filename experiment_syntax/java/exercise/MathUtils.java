class MathUtils {
    private static int square(int x) {
        return x*x;
    }

    public static void printSquare(int x) {
        int result = square(x);
        // System.out.print("Square of " + x);
        // System.out.print(" is " + result);
        System.out.println("Square of " + x + " is " + result);

    }

    public static void main(String[] args) {
        // MathUtils.printSquare(5);
        MathUtils.square(5); // in this case CAN access private method because main is in the same class
    }
}