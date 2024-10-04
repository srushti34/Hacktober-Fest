// Question: Complete the function to find the largest element in an array.

class Main {
    public static int findLargest(int[] arr) {
        int largest = arr[0];
        for (int value : arr) {
            if (value > largest) {
                largest = value;
            }
        }
        return largest;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 5, 1};
        System.out.println("Largest element: " + findLargest(arr));
    }
}
