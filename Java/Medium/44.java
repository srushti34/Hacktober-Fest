// Question: Complete the function to find the Nth Fibonacci number using dynamic programming.

class Main {
    public static int fibonacciDP(int n) {
        if (n <= 1) return n;
        int[] fib = new int[n + 1];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        return fib[n];
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println("Fibonacci number " + n + ": " + fibonacciDP(n));
    }
}
