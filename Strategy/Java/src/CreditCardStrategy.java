
public class CreditCardStrategy extends PaymentStrategy{
    @Override
    public void pay() {
        System.out.println("credit card method");
    }
}
