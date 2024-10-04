// Question: Complete the function to find the factorial of a number using recursion.

class Main {
    public static int factorial(int n) {
        if (n == 0 || n == 1) return 1;
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.println("Factorial of " + n + ": " + factorial(n));
    }
}
