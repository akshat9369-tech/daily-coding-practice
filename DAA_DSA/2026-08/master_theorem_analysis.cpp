#include <iostream>
#include <cmath>

void analyze_recurrence(double a, double b, double k) {
    double log_b_a = std::log(a) / std::log(b);
    std::cout << "Recurrence T(n) = " << a << "T(n/" << b << ") + O(n^" << k << "):\n";
    if (k < log_b_a) {
        std::cout << "  Case 1: T(n) = Theta(n^" << log_b_a << ")\n";
    } else if (std::abs(k - log_b_a) < 1e-6) {
        std::cout << "  Case 2: T(n) = Theta(n^" << k << " * log n)\n";
    } else {
        std::cout << "  Case 3: T(n) = Theta(n^" << k << ")\n";
    }
}

int main() {
    analyze_recurrence(2, 2, 1); // Merge Sort
    analyze_recurrence(4, 2, 1);
    analyze_recurrence(2, 2, 2);
    return 0;
}
