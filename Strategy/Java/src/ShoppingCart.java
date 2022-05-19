import java.util.Vector;

public class ShoppingCart {
    private Vector<Item> items =new Vector<>();
    public void addItem(Item i){
        items.add(i);
    }
    public void pay(PaymentStrategy s){
        s.pay();
    }
}
