
// Expected Answer :
// Primary diagonal sum: 15
// Secondary diagonal sum: 15

#include <stdio.h>

int main() {
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int primary_sum = 0, secondary_sum = 0;

    for (int i = 0; i < 3; i++) {
        primary_sum += matrix[i][i];
        secondary_sum += matrix[i][3-i];
    }

    printf("Primary diagonal sum: %d\n", primary_sum);
    printf("Secondary diagonal sum: %d\n", secondary_sum);

    return 0;
}