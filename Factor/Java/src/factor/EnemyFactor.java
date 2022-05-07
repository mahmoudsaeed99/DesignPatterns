package factor;

public class EnemyFactor {
    public static Enemy createEnemy(int id){
        switch (id){
            case 1:
                return new Bird();
            case 2:
                return new Turtle();
            default:
                return null;
        }

    }
}
