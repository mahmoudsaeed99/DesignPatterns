package Observer;

public class main {
    public static void main(String[] args) {
        product phone = new product("phone");
        person mahmoud = new person("mahmoud");
        person mohamed = new person("mohamed");
        person marwan = new person("marwan");

        phone.add(mahmoud);
        phone.add(mohamed);
        phone.add(marwan);

        for(int i=0 ;i<5;i++){
            boolean available = i%2==0 ;
            phone.setAvailability(available);
            if(i==2){
                phone.remove(marwan);
            }
            try {Thread.sleep(1000);} catch (InterruptedException ie){}
            System.out.println("-------------------------------------------------");
        }
        phone.setAvailability(true);
    }
}
