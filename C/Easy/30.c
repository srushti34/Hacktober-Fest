#include <stdio.h>

int main() {
    char grade;
    printf("Enter your grade (A, B, C, D, or F): ");
    scanf(" %c", &grade);
    
    switch(grade) {
        case 'A':
            printf("Excellent!");
            break;
        case 'B':
            printf("Good job!");
            break;
        case 'C':
            printf("Average performance.");
            break;
        case 'D':
            printf("Need improvement.");
            break;
        case 'F':
            printf("Failed.");
            break;
    }
    return 0;
}
