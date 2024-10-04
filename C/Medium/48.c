
#include <stdio.h>
void recurse() {
    printf("Recursing...\n");
    recurse(); 
}
int main() {
    recurse();
    return 0;
}
