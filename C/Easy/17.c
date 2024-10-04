#include <stdio.h>

int main() {
    int a = 10, *p;
    p = &a;
    printf("Value of a: %d", *a); // Wrong pointer dereference
    return 0;
}