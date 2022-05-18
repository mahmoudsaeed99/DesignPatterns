package command;

import java.util.Arrays;

public class RemoteControl {
    private Command[] onCommands;
    private Command[] offCommands;
    public RemoteControl(){
        onCommands = new Command[4];
        offCommands = new Command[4];
        NoCommand noCommand = new NoCommand();
        for(int i=0;i<onCommands.length;i++){
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
    }
    public void addCommand(int slot , Command onCommand , Command offCommand){
        onCommands[slot] = onCommand;
        offCommands[slot] = offCommand;

    }
    public void onButtonPressed(int slot){
        onCommands[slot].execute();
    }
    public void offButtonPressed(int slot){
        onCommands[slot].undo();
    }

    @Override
    public String toString() {
        StringBuffer buffer = new StringBuffer();
        for(int i=0 ; i<onCommands.length ; i++){
            buffer.append(String.format("[slot %d] %s \t %s%n",i,onCommands[i].getClass().getSimpleName(),offCommands[i].getClass().getSimpleName()));

        }
        return buffer.toString();
    }
}
