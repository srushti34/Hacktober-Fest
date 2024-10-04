// Complete the code to print size of array

#include <stdio.h>
 
void printArray(int arr[]) {
    printf("%d", sizeof(arr)); 
}
 
int main() {
	int arr[5];
	printArray(arr);
	return 0;
}
