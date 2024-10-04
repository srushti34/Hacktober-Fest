// Question: Complete the function to find and print all duplicate elements in an array.

import java.util.HashSet;

class Main {
    public static void findDuplicates(int[] arr) {
        HashSet<Integer> seen = new HashSet<>();
        HashSet<Integer> duplicates = new HashSet<>();
        
        for (int num : arr) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }
        
        for (int duplicate : duplicates) {
            System.out.println("Duplicate: " + duplicate);
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 2, 3, 6};
        findDuplicates(arr);
    }
}
