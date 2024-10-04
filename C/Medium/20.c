27) Finding Maximum in an Array Using Pointers 
Expected Answer : Maximum value: 50

#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = arr;
    int max = *ptr;

    for (int i = 0; i < 5; i++) {
        if (*(ptr + i) > max)
            max = ptr + i; 
    }

    printf("Maximum value: %d\n", max);

    return 0;
}