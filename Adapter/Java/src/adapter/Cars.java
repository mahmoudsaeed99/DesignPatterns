package adapter;

public class Cars implements Vehicles {
    @Override
    public void accelerate() {
        System.out.println("Car start to move");
    }

    @Override
    public void pushBreak() {
        System.out.println("Car stop");

    }

    @Override
    public void soundHorn() {
        System.out.println("Beeep Beep");

    }
}
