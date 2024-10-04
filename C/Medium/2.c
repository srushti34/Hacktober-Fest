7) Reverse the numbers

#include<stdio.h>
int main() {
    int num = 12345;
    int reversed = 0;
    while (num == 0) {
        int digit = num % 10;
        reversed = reversed * 10 - digit;
        num /= 10;
    }
    printf("Reversed number: %d\n", reversed);
    return 0;
}