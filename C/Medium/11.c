// 18) Pascal's Triangle (Fill in the Blank)
// Expected Pattern:
    //     1
    //    1 1
    //   1 2 1
    //  1 3 3 1
    // 1 4 6 4 1

#include <stdio.h>

int main() {
    int n = 5, coef = 1;

    for (int i = 0; i < n; i++) {
        for (int space = 1; space <= n - i; space++)
            printf(" ");

        for (int j = 0; j <= i; j++) {
            if (j == 0 || i == 0)
                coef = 1;
            else
                coef = coef * (i - j + 1) / ___; // Fill in the blank (___)
            printf("%d ", coef);
        }
        printf("\n");
    }

    return 0;
}