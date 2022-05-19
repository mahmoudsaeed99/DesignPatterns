
public class main {
    public static void main(String[] args) {
        Item item1 = new Item("111",20);
        Item item2 = new Item("222",40);
        Item item3 = new Item("333",60);
        Item item4 = new Item("444",80);
        ShoppingCart shop = new ShoppingCart();
        shop.addItem(item1);
        shop.addItem(item2);
        shop.addItem(item3);
        shop.addItem(item4);
        shop.pay(new PaypalStrategy());
    }
}
