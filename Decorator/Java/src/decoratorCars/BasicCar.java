package decoratorCars;

public class BasicCar implements Car{
    @Override
    public double getcost() {
        return 35000;
    }

    @Override
    public String getDescription() {
        return "car";
    }
}
