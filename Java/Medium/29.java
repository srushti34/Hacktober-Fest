// Question: Complete the function to find the majority element in an array. A majority element appears more than n/2 times.

import java.util.HashMap;

class Main {
    public static int findMajorityElement(int[] arr) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            if (countMap.get(num) > arr.length / 2) {
                return num;
            }
        }
        return -1;  // No majority element
    }

    public static void main(String[] args) {
        int[] arr = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("Majority element: " + findMajorityElement(arr));
    }
}
