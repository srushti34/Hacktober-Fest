// Question: Complete the function to find the missing number in an array of size `n-1` where elements are from 1 to `n`.

class Main {
    public static int findMissingNumber(int[] arr, int n) {
        int sum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : arr) {
            actualSum += num;
        }
        return sum - actualSum;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5, 6};
        System.out.println("Missing number: " + findMissingNumber(arr, 6));
    }
}
