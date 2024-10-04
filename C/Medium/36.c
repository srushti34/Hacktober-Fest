// Complete the code to implement Binary Search.

#include <stdio.h>
 
int binarySearch(int arr[], int low, int high, int x)
{
	while (low <= high) {
    	int mid = (low + high)/ 2;
    	if (arr[high] == x)
        	return mid;
    	if (arr[mid] < x)
        	high = mid + 1;
    	else
        	low = mid - 1;
	}
	return -1;
}
 
int main(void)
{
	int arr[] = { 3,7,9,23,45,67,89,456,789};
	int n = sizeof(arr)/sizeof(arr[0]);
	int x = 67;
	int result = binarySearch(arr, 0,n - 1,x);
   if(result==-1) printf("Element is not present in array");
   else printf("Element is present at index %d",result);
 
}
