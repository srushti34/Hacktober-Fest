// Question: Complete the function to find the intersection (common elements) of two arrays.

import java.util.HashSet;

class Main {
    public static void findIntersection(int[] arr1, int[] arr2) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : arr1) {
            set.add(num);
        }

        for (int num : arr2) {
            if (set.contains(num)) {
                System.out.println("Common element: " + num);
            }
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {4, 5, 6, 7, 8};
        findIntersection(arr1, arr2);
    }
}
