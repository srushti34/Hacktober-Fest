// Question: Complete the function to find and print all permutations of a string.

class Main {
    public static void permute(String str, String answer) {
        if (str.length() == 0) {
            System.out.println(answer);
            return;
        }

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            String leftSubstr = str.substring(0, i);
            String rightSubstr = str.substring(i + 1);
            permute(leftSubstr + rightSubstr, answer + ch);
        }
    }

    public static void main(String[] args) {
        String str = "ABC";
        permute(str, "");
    }
}
