package command;

public class turnOnTv implements Command{
    private Tv tv;
    public turnOnTv(Tv tv){
        this.tv = tv;
    }


    @Override
    public void execute() {
        this.tv.turnOn();
    }

    @Override
    public void undo() {
        this.tv.turnOff();

    }
}
