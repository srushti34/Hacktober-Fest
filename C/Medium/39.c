// Complete the code to compare string value to enter a password

#include <stdio.h>
#include <string.h> 

int main() {
    char default = "Invalid TRY AGAIN!"; 
    char password = "password";    
    char entered_pass[50];           
    
    printf("Enter password: ");
    scanf("%c", entered_pass); 
    if (___(entered_pass, password) == 0) {
        printf("Logged in!\n");
    }
    else {
        printf("%s\n", default); 
    }
    
    return 0;
}
