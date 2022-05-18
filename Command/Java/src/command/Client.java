package command;

public class Client {
    public static void main(String[] args) {

        Light light = new Light();
        Tv tv = new Tv();

        RemoteControl remoteControl = new RemoteControl();


        turnOnLight turnOnLightCommand = new turnOnLight(light);
        turnOffLight turnOffLightCommand = new turnOffLight(light);
        turnOnTv turnOnTvCommand = new turnOnTv(tv);
        turnOffTv turnOffTvCommand = new turnOffTv(tv);

        remoteControl.addCommand(0,turnOnLightCommand ,turnOffLightCommand);
        remoteControl.addCommand(1,turnOnTvCommand ,turnOffTvCommand);

        remoteControl.onButtonPressed(0);
        remoteControl.onButtonPressed(1);
        remoteControl.offButtonPressed(0);
        remoteControl.offButtonPressed(1);
        System.out.println(remoteControl.toString());
    }




}
