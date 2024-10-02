#include <iostream>
using namespace std;
void func(int);
int main()
{
    func();
    return 0;
}
void func(int x)
{
    cout << x << endl;
}
