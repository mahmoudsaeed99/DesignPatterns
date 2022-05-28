package template;

public class main {
    public static void main(String[] args) {
        CSVDataParser csv = new CSVDataParser();
        csv.parseDataAndGenerateOutput();
        System.out.println("------------------------------------");
        DatabaseDataParser db = new DatabaseDataParser();
        db.parseDataAndGenerateOutput();

    }
}
