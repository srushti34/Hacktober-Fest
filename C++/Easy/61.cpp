#include <iostream>
using namespace std;
int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    int *ptr = arr;
    ptr += 10;
    cout << *ptr << endl;
    return 0;
}
