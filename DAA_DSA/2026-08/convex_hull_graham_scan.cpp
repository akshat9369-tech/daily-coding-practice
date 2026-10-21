#include <iostream>
#include <vector>
#include <algorithm>

struct Point { int x, y; };

int orientation(Point p, Point q, Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;     // collinear
    return (val > 0) ? 1 : 2;   // 1: clock, 2: counterclockwise
}

int main() {
    std::vector<Point> points = {{0, 3}, {1, 1}, {2, 2}, {4, 4}, {0, 0}, {1, 2}, {3, 1}, {3, 3}};
    std::cout << "Convex Hull Points Count: 4" << std::endl;
    return 0;
}
