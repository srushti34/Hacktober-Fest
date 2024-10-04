#include <stdio.h>

void print_elements(int _____, int size) {   
    for (int i = 0; i _ size; i++) { 
        printf("%d\n", elements[i]);  
    }
}

int main() {
    int elements[] = {1, 2, 3}; 
    int size = ____(elements) / ____(elements[0]);  
    print_elements(_____, size);  
    return 0;
}