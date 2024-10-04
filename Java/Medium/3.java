// Question: Complete the Fibonacci sequence algorithm using recursion, but ensure it is optimized to handle large input values.

class Main {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        int n = 10;  // Test with the 10th Fibonacci number
        System.out.println("Fibonacci number " + n + ": " + fibonacci(n));
    }
}
