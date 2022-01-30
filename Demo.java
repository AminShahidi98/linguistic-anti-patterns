public class Demo {
   
    static int isChecked=6;
    static int isDobed=9;
    static int[] cv = {23, 34, 533};
    int getMyFood = 3;
    
    public static void main(String[] args) {
        System.out.print(isValid(-11)); 
    }

    private static int[] yesisMethode(int[] x, String m) {
        System.out.print(m);
        return x;
    }



    public static void calculateForgetMyFood(String star) {
        System.out.print(star);
    }
    
    int isFalse = 1;



    public static int getisDobed(int d, String star) {
    return complement_getisDobed(d, star);
    }

    public static int getyourDobed(int d, String star) {
    return complement_getyourDobed(d, star);
    }

    public static boolean isValid(int d) {
    double[] temp = complement_isValid(d);
    int size = temp.length;
    if (size == 0) {return false;}
    else if (size == 1){
        double tempDouble = temp[0];
        if (tempDouble == 0) {return false;}
        else {return true;}
    }
    else {return true;}
    }


    public static int complement_getisDobed(int d, String star) {
        isDobed *= d;
        return isDobed;
    }

    public static int complement_getyourDobed(int d, String star) {
        isDobed *= d;
        return isDobed;
    }

    public static double[] complement_isValid(int d) {
        if (d == 5) {
            return new double[] {23};
        }
        else if (d == 4) {
            double[] testS = {-23, 42};
            return testS;
        }
        else if (d == 9) {
            return new double[] {66};
        }
        else if (d == -11) {
            double[] testS2 = {0.0d};
            return testS2;
        }
        else if (d == -2) {
            double[] testS2 = {};
            return testS2;
        }
        else {
            return new double[] {1};
        }
    }
}