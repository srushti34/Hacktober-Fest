// 21) Pointer Arithmetic (Fill in the Blank)

#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // Pointer to the first element

    printf("Initial value: %d\n", *ptr);

    // Increment pointer
    ptr = ___;  // Fill in the blank
    printf("After incrementing pointer: %d\n", *ptr);

    // Decrement pointer
    ptr = ___;  // Fill in the blank
    printf("After decrementing pointer: %d\n", *ptr);

    return 0;
}