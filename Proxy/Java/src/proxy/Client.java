package proxy;

import java.util.Arrays;
import java.util.List;

public class Client {
    public static void main(String[] args) {
        List<String> blockSites = Arrays.asList("facebook","twitter","google","youtube");
        ISP internet = new InternetProxy();
        for (String string:blockSites){
            System.out.println(internet.serverSite(string));
        }

    }
}
