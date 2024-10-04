#include <stdio.h>

int main() {
    int i = 0;

label:
    if (i < 10) {
        if (i__5) {
            i++; 
            goto label; 
        }
        printf("%d\n", i);
        i++;
        ___ label; 
    }

    return 0;
}
