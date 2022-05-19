package decoratorSandwich;

public abstract class  SandwichDecorator implements Sandwich {
    private Sandwich sandwich;
    public SandwichDecorator(Sandwich sandwich){
        this.sandwich = sandwich;
    }

    @Override
    public String getDescription() {
        return this.sandwich.getDescription();
    }

    @Override
    public double getcost() {
        return this.sandwich.getcost();
    }
}
