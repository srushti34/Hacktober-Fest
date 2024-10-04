
#include <stdlib.h>
int main() {
    int *ptr = (int *)malloc(sizeof(int));
    // Missing free(ptr);
    return 0;
}