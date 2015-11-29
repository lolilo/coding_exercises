

public class Person {

    public String name;
    public int age; 

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }


    public void sayName() {
        println(name);
    }

    public static void sayLatinName() {
        println('Homo Sapiens');
    }

}

Person p = new Person('Liana', 23);
p.sayName(); // Liana
p.sayLatinName(); // Homo Sapiens

Person.sayLatinName(); // Homo Sapiens


