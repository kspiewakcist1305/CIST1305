#include <iostream>

int some_number = 5;

using namespace std;

void main()
{
    some_number == 5 ? std::cout << "It's 5" : std::cout << "It's not 5";

    if (some_number == 5)
    {
        std::cout << "It's 5";
    }
    else
    {
        std::cout << "It's not 5";
    }
}
