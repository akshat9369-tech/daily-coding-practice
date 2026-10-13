#include <iostream>
#include <vector>

class FenwickTree {
    std::vector<int> tree;
public:
    FenwickTree(int n) : tree(n + 1, 0) {}
    void update(int i, int delta) {
        for (; i < (int)tree.size(); i += i & (-i)) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & (-i)) sum += tree[i];
        return sum;
    }
};

int main() {
    FenwickTree bit(10);
    bit.update(3, 5);
    bit.update(5, 2);
    std::cout << "Prefix sum up to 5: " << bit.query(5) << std::endl;
    return 0;
}
