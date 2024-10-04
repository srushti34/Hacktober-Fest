// Question: Complete the function to check if one string is a rotation of another string.

class Main {
    public static boolean areRotations(String str1, String str2) {
        return (str1.length() == str2.length()) && ((str1 + str1).contains(str2));
    }

    public static void main(String[] args) {
        String str1 = "ABCD";
        String str2 = "CDAB";
        System.out.println("Are rotations: " + areRotations(str1, str2));
    }
}
