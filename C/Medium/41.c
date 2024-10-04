int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};  
    int size = ___(arr) / ___(arr[0]);  

    printf("Original array:\n");
    for (int i = 0; i <___; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    
    for (int i = 0; i <___; i++) {
        if (arr[i] % 2 ___ 0) {  
            arr[i] *= 2;  
        }
    }

    printf("Modified array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}