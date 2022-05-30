package proxy;

import java.util.Arrays;
import java.util.List;

public class InternetProxy implements ISP {
    private List<String> blockSites = Arrays.asList("facebook","twitter");
    @Override
    public String serverSite(String url) {
        logSite(url);
        if(blockSites.contains(url)){
            return "\nthis site is blocked\n";
        }
        return  new Etisalat().serverSite(url);
    }
    public void logSite(String url){
        System.out.printf(" [%d] %s",System.currentTimeMillis(),url);
    }
}
