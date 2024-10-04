// Question: Complete the function to move all zeros to the end of an array without changing the order of non-zero elements.

class Main {
    public static void moveZerosToEnd(int[] arr) {
        int nonZeroIndex = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                arr[nonZeroIndex++] = arr[i];
            }
        }

        while (nonZeroIndex < arr.length) {
            arr[nonZeroIndex++] = 0;
        }
    }

    public static void main(String[] args) {
        int[] arr = {0, 1, 0, 3, 12};
        moveZerosToEnd(arr);
        for (int value : arr) {
            System.out.print(value + " ");
        }
    }
}
