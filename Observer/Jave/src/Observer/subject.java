package Observer;

public interface subject {
    void add(observer observ);
    void remove(observer observ);
    void notifyallObserver();
}

