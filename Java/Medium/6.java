// Question: Complete the function to check if a given string is a palindrome (the same forwards and backwards).

class Main {
    public static boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        String str = "racecar";
        System.out.println("Is palindrome: " + isPalindrome(str));
    }
}
