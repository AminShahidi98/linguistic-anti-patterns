public class Demo {
   
    int isChecked=6;
    static int isDobed=9;
    static int[] cv = {23, 34, 533};
    
    public static void main(String[] args) {
        System.out.print(getisDobed(2));
    }
    private static int[] instanceMethode(int[] x, String m) {
        System.out.print(m);
        return x;
    }
    public static int getisDobed(int d) {
        isDobed *= d;
        return isDobed;
    }
}