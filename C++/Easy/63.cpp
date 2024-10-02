#include <iostream>
int add(float a, float b);
int main()
{
    std::cout << add(3, 4) << std::endl;
}
int add(float a, float b)
{
    return a + b;
}
