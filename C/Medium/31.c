// Complete the code to find a duplicate number in an array of size n where each number appears exactly twice except for one number which appears once.

#include <stdio.h>
int main() {
    int arr[] = {1, 2, 3, 4, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int max = n;
    int count[max + 1];
    
    for (int i = 0; i <= max; i++) {  
        count[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        if (count[arr[i]] == 2) {  
            printf("The duplicate number is %d\n", arr[i]);
            break;
        }
        count[arr[i]]++;
    }
    return 0;
}
