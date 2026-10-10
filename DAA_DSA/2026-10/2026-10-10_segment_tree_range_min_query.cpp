#include <iostream>
#include <vector>
#include <algorithm>

class SegmentTree {
    std::vector<int> tree;
    int n;
public:
    SegmentTree(const std::vector<int>& arr) {
        n = arr.size();
        tree.resize(4 * n);
        build(arr, 1, 0, n - 1);
    }
    void build(const std::vector<int>& arr, int node, int start, int end) {
        if (start == end) tree[node] = arr[start];
        else {
            int mid = (start + end) / 2;
            build(arr, 2 * node, start, mid);
            build(arr, 2 * node + 1, mid + 1, end);
            tree[node] = std::min(tree[2 * node], tree[2 * node + 1]);
        }
    }
    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 1e9;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return std::min(query(2 * node, start, mid, l, r),
                        query(2 * node + 1, mid + 1, end, l, r));
    }
};

int main() {
    std::vector<int> arr = {1, 3, 2, 7, 9, 11};
    SegmentTree st(arr);
    std::cout << "RMQ in range [1, 4]: " << st.query(1, 0, arr.size() - 1, 1, 4) << std::endl;
    return 0;
}
