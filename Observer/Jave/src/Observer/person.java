package Observer;

public class person implements observer{
    private String name;
    public person(String name){
        this.name = name;
    }


    @Override
    public void update(String message) {
        System.out.printf("%s got new notification: %s%n ",this.name,"  "+message);
    }
}
