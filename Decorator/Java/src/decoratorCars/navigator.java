package decoratorCars;

public class navigator extends CarDecorator {
    public navigator(Car car) {
        super(car);
    }

    @Override
    public String getDescription() {
        return super.getDescription()+ "  navigator";
    }

    @Override
    public double getcost() {
        return super.getcost() + 2500;
    }
}
