// 20) Hollow Square with Diagonals (Fill in the Blank)
// Expected Pattern:
// * * * * *
// * *   * *
// *   *   *
// * *   * *
// * * * * *

#include <stdio.h>

int main() {
    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == 1 || i == n || ___ || ___ || i == j || ___ == n + 1) // Fill in the blanks (___)
                printf("* ");
            else
                printf("  ");
        }
        printf("\n");
    }

    return 0;
}