package template;

public class DatabaseDataParser extends DataParser {
    @Override
    void readDate() {
        System.out.println("read Database");
    }

    @Override
    void processDate() {
        System.out.println("process Database");
    }
}
