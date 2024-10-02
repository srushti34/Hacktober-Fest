#include <iostream>
using namespace std;
int main()
{
    int *ptr = new int(5);
    delete ptr;
    cout << *ptr << endl;
    return 0;
}
