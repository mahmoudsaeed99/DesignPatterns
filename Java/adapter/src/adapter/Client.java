package adapter;

public class Client {
    public static void main(String[] args) {
        Vehicles car = new Cars();
        playWithVehicles(car);
        Vehicles bicycle = new BicycleAdapter(new Bicycle());
        playWithVehicles(bicycle);


    }
    private static void playWithVehicles(Vehicles vehicles){
        vehicles.accelerate();
        vehicles.pushBreak();
        vehicles.soundHorn();
        System.out.println("-------------------------------------------");

    }
}
