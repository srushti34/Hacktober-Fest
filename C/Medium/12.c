// 19)  Hollow Pyramid Pattern (Fill in the Blank)
//     *
//    * *
//   *   *
//  *     *
// *********

#include <stdio.h>

int main() {
    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++)
            printf(" ");

        for (int k = 1; k <= 2 * i - 1; k++) {
            if (i == ___ || k == 1 || k == ___) // Fill in the blanks (___)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }

    return 0;
}