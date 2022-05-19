package decoratorSandwich;

public class fool extends SandwichDecorator {

    public fool(Sandwich sandwich) {
        super(sandwich);
    }

    @Override
    public double getcost() {
        return super.getcost() +2.0;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + "  fool";
    }
}
