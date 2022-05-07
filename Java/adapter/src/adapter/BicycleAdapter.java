package adapter;

public class BicycleAdapter implements Vehicles {
    private Bicycle bicycle;
    public BicycleAdapter(Bicycle bicycle){
        this.bicycle = bicycle;

    }

    @Override
    public void accelerate() {
    bicycle.pedal();
    }

    @Override
    public void pushBreak() {
        bicycle.stop();
    }

    @Override
    public void soundHorn() {
        bicycle.ringBell();
    }
}
