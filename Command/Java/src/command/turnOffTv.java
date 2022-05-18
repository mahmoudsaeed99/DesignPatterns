package command;

public class turnOffTv implements Command{
    private Tv tv;
    public turnOffTv(Tv tv){
        this.tv = tv;
    }


    @Override
    public void execute() {
        this.tv.turnOff();
    }

    @Override
    public void undo() {
        this.tv.turnOn();

    }
}
