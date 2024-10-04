11) Recursive Function

#include <stdio.h>

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n); 
}

int main() {
    printf("Factorial: %d\n", factorial(5));
    return 0;
}
