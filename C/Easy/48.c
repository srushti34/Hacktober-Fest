#include <stdio.h>

int infinite_recursion(int n) {
    if (n > 10) {
        return n;  // Base case
    }
    return infinite_recursion(n + 1);  // Recursive call with increment
}

int main() {
    int result = infinite_recursion(0);
    printf("%d\n", result);  // Print the result
    return 0;
}
