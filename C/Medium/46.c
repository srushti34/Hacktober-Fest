
#include <stdio.h>
#include <stdlib.h>
int main() {
    int *arr = malloc(5 * sizeof(int));
    arr[5] = 10;
    printf("%d\n", arr[5]);
    free(arr);
    return 0;
}
