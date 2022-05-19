package decoratorSandwich;

public class BasicSandwich implements Sandwich {
    @Override
    public double getcost() {
        return 10;
    }

    @Override
    public String getDescription() {
        return "Bread";
    }
}
