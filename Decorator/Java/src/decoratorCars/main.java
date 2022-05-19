package decoratorCars;

public class main {
    public static void main(String[] args) {
        Car basicCar = new BasicCar();
        System.out.println("cost  "+basicCar.getcost());
        System.out.println("desc  "+basicCar.getDescription());
        Car extendCar = new cdRoom(new navigator(new BasicCar()));
        Car extendCar2 = new navigator(new cdRoom(new BasicCar()));
        System.out.println("cost:  "+extendCar.getcost());
        System.out.println("desc:  "+extendCar.getDescription());
        System.out.println("cost:  "+extendCar2.getcost());
        System.out.println("desc:  "+extendCar2.getDescription());



    }
}
