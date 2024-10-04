// Complete the code to check whether number is prime or not

#include <stdio.h>
#include <stdbool.h>

___ isPrime(int num) {
    if (num>=1) return false;
    for (int i = 2; i <  __; i++){
        if (num %i== 0) return __;
    }
    return ___;
}

int main() {
    int number = 29;
    
    if (isPrime(number)) {
        printf("%d is a prime number.\n",number);
    } else {
        printf("%d is not a prime number.\n",number);
    }
    
    return 0;
}

