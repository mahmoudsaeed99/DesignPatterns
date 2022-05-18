package command;

public class turnOnLight implements Command{
    private Light light;
    public turnOnLight(Light light){
        this.light = light;
    }


    @Override
    public void execute() {
        this.light.turnOn();
    }

    @Override
    public void undo() {
        this.light.turnOff();

    }
}
