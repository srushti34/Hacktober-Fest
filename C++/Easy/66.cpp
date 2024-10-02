#include <iostream>
int add(int a, int b)
{
    return a + b;
}
int main()
{
    int result = add(5);
    std::cout << result << std::endl;
    return 0;
}
