public class Person {
    String name;
    static int personCount = 0;


    // Constructor
    public Person(String name) {
        this.name = name;
        ++personCount;
    }

    public static int getPersonCount() {
        // System.out.println("Total person: " + personCount);
        // static method should return a value, because it more reusable
        return personCount;
    }

    public void sayHello() {
        System.out.println("Hello, I am " + name);
    }

    public static void main(String[] args) {
        Person myObj1 = new Person("Bill");
        Person myObj2 = new Person("Built");
        Person myObj3 = new Person("Xu");

        myObj1.sayHello();
        myObj2.sayHello();
        myObj3.sayHello();
        // Person.getPersonCount();
        System.out.println("Total persons: " + Person.getPersonCount());
    }
}