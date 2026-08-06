#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cfloat>

struct Point { double x, y; };

double dist(Point p1, Point p2) {
    return std::sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y));
}

double brute_force(const std::vector<Point>& P, int n) {
    double min_d = DBL_MAX;
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            min_d = std::min(min_d, dist(P[i], P[j]));
    return min_d;
}

int main() {
    std::vector<Point> P = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
    std::cout << "Closest pair distance: " << brute_force(P, P.size()) << std::endl;
    return 0;
}
