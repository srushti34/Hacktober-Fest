// 25) Fibonacci Series Using Iteration (Fill in the Blank)

#include <stdio.h>

int main() {
    int n, t1 = 0, t2 = 1, nextTerm;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: %d %d ", t1, t2);

    for (int i = 3; i <= n; i++) {
        nextTerm = ___ + ___;  // Fill in the blank
        printf("%d ", nextTerm);
        t1 = ___;  // Fill in the blank
        t2 = ___;  // Fill in the blank
    }

    return 0;
}
