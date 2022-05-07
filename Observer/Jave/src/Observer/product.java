package Observer;

import java.util.ArrayList;
import java.util.List;
import java.util.Observer;

public class product implements  subject{
    private String name;
    private String availability;
    private List<observer> observersList;
    public product(String name){
        this.name = name;
        this.observersList = new ArrayList<>();
    }

    @Override
    public void add(observer observ) {
        this.observersList.add(observ);
    }

    @Override
    public void remove(observer observ) {
        this.observersList.remove(observ);
    }

    @Override
    public void notifyallObserver() {
        for(observer observ : observersList){
            observ.update(availability);
        }
    }
    public void setAvailability(boolean availbile){
        availability = availbile? "available":"not available";
        notifyallObserver();
    }
}
