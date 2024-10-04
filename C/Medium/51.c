
#include <stdio.h>
void myFunction(int a);
int main() {
    myFunction(5.5);
    return 0;
}
void myFunction(int a) {
    printf("%d\n", a);
}
