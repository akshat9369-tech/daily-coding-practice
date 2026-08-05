#include <iostream>
#include <cmath>
#include <string>

long long karatsuba(long long x, long long y) {
    if (x < 10 || y < 10) return x * y;

    std::string s_x = std::to_string(x);
    std::string s_y = std::to_string(y);
    int n = std::max(s_x.length(), s_y.length());
    int m = n / 2;

    long long divisor = std::pow(10, m);
    long long high1 = x / divisor, low1 = x % divisor;
    long long high2 = y / divisor, low2 = y % divisor;

    long long z0 = karatsuba(low1, low2);
    long long z1 = karatsuba(low1 + high1, low2 + high2);
    long long z2 = karatsuba(high1, high2);

    return z2 * std::pow(10, 2 * m) + (z1 - z2 - z0) * divisor + z0;
}

int main() {
    long long a = 1234, b = 5678;
    std::cout << "Karatsuba(" << a << ", " << b << ") = " << karatsuba(a, b) << std::endl;
    std::cout << "Standard product: " << (a * b) << std::endl;
    return 0;
}
