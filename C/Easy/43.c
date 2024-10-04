#include <stdio.h>

union MyUnion {
    int x;
    char c;
};

int main() {
    union MyUnion myUnion;
    myUnion.x = 10;
    myUnion.c = 'A'; 
    return 0;
}
