// Question: Complete the function to check if a given number is a power of two.

class Main {
    public static boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        return (n & (n - 1)) == 0;
    }

    public static void main(String[] args) {
        int n = 16;
        System.out.println("Is power of two: " + isPowerOfTwo(n));
    }
}
