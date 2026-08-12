#include <iostream>
#include <vector>
#include <algorithm>

struct Job { char id; int deadline, profit; };

bool cmp_profit(Job a, Job b) { return a.profit > b.profit; }

int main() {
    std::vector<Job> jobs = {{'a', 4, 20}, {'b', 1, 10}, {'c', 1, 40}, {'d', 1, 30}};
    std::sort(jobs.begin(), jobs.end(), cmp_profit);

    int max_deadline = 4;
    std::vector<char> slots(max_deadline + 1, '-');
    int total_profit = 0;

    for (const auto& j : jobs) {
        for (int d = std::min(max_deadline, j.deadline); d > 0; d--) {
            if (slots[d] == '-') {
                slots[d] = j.id;
                total_profit += j.profit;
                break;
            }
        }
    }

    std::cout << "Scheduled Jobs: ";
    for (int d = 1; d <= max_deadline; d++) if (slots[d] != '-') std::cout << slots[d] << " ";
    std::cout << "\nTotal Profit: " << total_profit << std::endl;
    return 0;
}
