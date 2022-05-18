package command;

public class turnOffLight implements Command{
    private Light light;
    public turnOffLight(Light light){
        this.light = light;
    }


    @Override
    public void execute() {
        this.light.turnOff();
    }

    @Override
    public void undo() {
        this.light.turnOn();

    }
}
