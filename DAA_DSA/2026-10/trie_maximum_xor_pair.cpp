#include <iostream>
#include <vector>
#include <algorithm>

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
};

void insert(TrieNode* root, int num) {
    TrieNode* curr = root;
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (!curr->children[bit]) curr->children[bit] = new TrieNode();
        curr = curr->children[bit];
    }
}

int find_max_xor(TrieNode* root, int num) {
    TrieNode* curr = root;
    int max_xor = 0;
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        int opp = 1 - bit;
        if (curr->children[opp]) {
            max_xor |= (1 << i);
            curr = curr->children[opp];
        } else {
            curr = curr->children[bit];
        }
    }
    return max_xor;
}

int main() {
    std::vector<int> nums = {3, 10, 5, 25, 2, 8};
    TrieNode* root = new TrieNode();
    for (int x : nums) insert(root, x);

    int ans = 0;
    for (int x : nums) ans = std::max(ans, find_max_xor(root, x));
    std::cout << "Maximum XOR pair value: " << ans << std::endl;
    return 0;
}
