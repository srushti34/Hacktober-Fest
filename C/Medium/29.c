#include <stdio.h>
struct {
    int x;
} myStruct;
int main() {
    printf("%d", myStruct.x);
    return 0;
}
