// Expected Answer: Result of addition: 30

#include <stdio.h>
int add(int a, int b) {
    return a + b;
}

int main {
    int (*func_ptr)(int, int);

    func_ptr = ___;  // Fill in the blank

    // Call the function using the pointer
    int result = func_ptr(10, 20); 

    printf("Result of addition: %d\n", result);

    return 0;
}