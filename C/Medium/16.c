// 23) Memory Allocation Using malloc (Fill in the Blank)

#include <stdio.h>
#include <stdlib.h>  
int main() {
    int *arr;
    int n;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Allocate memory for n elements
    arr = (int*) ___;  // Fill in the blank

    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }


    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }


    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    printf("\n");

    // Free the allocated memory
    ___;  // Fill in the blank

    return 0;
}