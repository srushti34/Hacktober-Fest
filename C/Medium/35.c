// Complete the code to find the second smallest element in an array of integers.

#include <stdio.h>

int main() {
    int arr[] = {12, 13, 1, 10, 34, 16};
    int n = sizeof(arr) / sizeof(arr[0]);
    int first, second;
    
    first = second = -1;

    for (int i = 0; i < n; i++) {
        if (arr[i] < first) {
            second = first;
            first = arr[i];
        } else if (arr[i] < second && arr[i] != first) {
            second = arr[i];
        }
    }

    if (second == -1)
        printf("No second smallest element.\n");
    else
        printf("The second smallest element is %d\n", second);

    return 0;
}
