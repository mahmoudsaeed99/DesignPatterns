package decoratorCars;

public abstract class CarDecorator implements Car {
    private Car car;
    public CarDecorator(Car car){
        this.car = car;
    }
    @Override
    public double getcost() {
        return this.car.getcost();
    }

    @Override
    public String getDescription() {
        return this.car.getDescription();
    }
}
