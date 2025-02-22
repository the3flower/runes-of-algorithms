// Class and Method
public class JavaSyntax {
    public static void basicJava() {
        System.out.println("[How THINGS works?]");
        System.out.println("1. You need to Compile Java file first by (command) javac <filename>.java");
        System.out.println("2. After that it will generate .class file (bytecode)");
        System.out.println("3. JVM will read .class file by (command) java <filename>");
    }

    public static void basic() {
        System.out.println("[This is basic of Java mate]");
        int number = 10;
        double deci = 10.10;
        char a = 'a';
        boolean isActive = true;
        String word = "java javac";

        System.out.println("Number: " + number);
        System.out.println("Pre-decrement(--number): " + --number);
        System.out.println("Post-increment: " + number++);
        System.out.println("Final number: " + number);
    }

    public static void forLoop() {
        System.out.println("[For loop is here!]");

        int sum = 0;
        for(int i = 0; i < 100; i++) { // 0 - 99
            for(int j = 1; j <= 3; j++) { // 1 - 3
                sum += j;
            }
        }
        System.out.println(sum);
    }

    void instanceMethod() {
        System.out.println("[THIS IS Instance Method, I required object :)]");
    }

    public static void main(String[] args) {
        System.out.println("THIS IS JAVA NOTES GUYS");
        basicJava();
        forLoop();
        basic();

        // void instanceMethod()
        JavaSyntax obj = new JavaSyntax();
        obj.instanceMethod();
    }
}

