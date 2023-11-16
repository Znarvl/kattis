#include <iostream>
#include <sstream>

int main()
{

    int n, x;
    std::cin >> n >> x;
    int y = 0;

    std::string line;

    while (n != 0)
    {
        int a;
        std::cin >> a;
        y += a;
        n -= 1;
    }
    if (y <= x)
    {
        std::cout << "Jebb\n";
    }
    else
    {
        std::cout << "Neibb\n";
    }

    return 0;
}