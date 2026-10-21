#include <iostream>
#include <vector>
#include <algorithm>

struct Activity { int start, finish; };

bool activity_cmp(Activity a, Activity b) {
    return a.finish < b.finish;
}

int main() {
    std::vector<Activity> acts = {{1, 2}, {3, 4}, {0, 6}, {5, 7}, {8, 9}, {5, 9}};
    std::sort(acts.begin(), acts.end(), activity_cmp);

    std::cout << "Selected Activities: ";
    int last_finish = -1;
    for (const auto& a : acts) {
        if (a.start >= last_finish) {
            std::cout << "[" << a.start << ", " << a.finish << "] ";
            last_finish = a.finish;
        }
    }
    std::cout << std::endl;
    return 0;
}
