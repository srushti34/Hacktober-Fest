// Question: Complete the function to find the first non-repeated character in a string.

import java.util.HashMap;

class Main {
    public static char firstNonRepeatedChar(String str) {
        HashMap<Character, Integer> charCount = new HashMap<>();
        for (char c : str.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        for (char c : str.toCharArray()) {
            if (charCount.get(c) == 1) {
                return c;
            }
        }
        return '\0';  // return null character if no non-repeated character found
    }

    public static void main(String[] args) {
        String str = "swiss";
        System.out.println("First non-repeated character: " + firstNonRepeatedChar(str));
    }
}
