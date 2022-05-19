package decoratorSandwich;

public class main {
    public static void main(String[] args) {
        Sandwich basicSandwich = new fool(new salad(new BasicSandwich()));


        System.out.printf("description:  %s%n",basicSandwich.getDescription());
        System.out.printf("cost %.2f%n",basicSandwich.getcost());
    }
}
