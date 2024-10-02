#include <iostream>
int add(int a, int b)
{
    return a + b + "result";
}
int main()
{
    std::cout << add(5, 3) << std::endl;
    return 0;
}
