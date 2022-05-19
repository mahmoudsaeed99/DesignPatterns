package decoratorSandwich;

public class salad extends SandwichDecorator {
    public salad(Sandwich sandwich) {
        super(sandwich);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + "  salad";

    }

    @Override
    public double getcost() {
        return super.getcost()+0.5;
    }
}
