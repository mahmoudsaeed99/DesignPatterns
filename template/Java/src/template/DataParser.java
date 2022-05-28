package template;

public abstract class DataParser {

        public void parseDataAndGenerateOutput(){
                readDate();
                processDate();
                writeDate();
        }
        abstract void readDate();
        abstract void processDate();
        public void writeDate(){
            System.out.println("writing");
        }
}
d