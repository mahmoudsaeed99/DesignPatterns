package decoratorCars;

public class cdRoom extends CarDecorator {
    public cdRoom(Car car) {
        super(car);
    }

    @Override
    public double getcost() {
        return super.getcost() + 1000;
    }

    @Override
    public String getDescription() {
        return super.getDescription()+"  cdRoom";
    }
}
