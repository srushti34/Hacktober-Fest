// Question: Complete the function to calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.

class Main {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        int a = 56, b = 98;
        System.out.println("GCD: " + gcd(a, b));
    }
}
