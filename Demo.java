public class Demo {
   
    String firstName, middleName, lastName;
    int age, averageScore, entranceYear;
    char sexuality;
    boolean isGraduated;
    static int studentsCount;
    
    public static void main(String[] args) {
        System.out.print("Hello world");
    }


    
    public boolean isStudentGraduated() {
    int temp = complement_isStudentGraduated();
    if (temp == 0) {return false;}
    else {return true;}
    }

    public void calculateForgetFullName() {
        String fullName = firstName + " " + middleName + " " + lastName;
        System.out.print(fullName);
    }

    public int getAverageScore() {
    return complement_getAverageScore();
    }

    public String logFor_setGraduationStatus;
    public void setGraduationStatus_WithLog(int status) {
        if (status == 1){
            isGraduated = true;
             logFor_setGraduationStatus =  "Set to true";
        }
        else if (status == 0){
            isGraduated = false;
             logFor_setGraduationStatus =  "Set to false";
        }
        else {
             logFor_setGraduationStatus =  "Method input must be 0 or 1!";
        }
    }


    public int complement_getAverageScore() {
        int tempAverageScore;
        tempAverageScore = averageScore + 1;
        if(tempAverageScore >= 20){
            return 20;
        }
        else {
            return tempAverageScore;
        }
    }

    public int complement_isStudentGraduated() {
        if(isGraduated){
            return 1;
        }
        else {
            return 0;
        }
    }
}