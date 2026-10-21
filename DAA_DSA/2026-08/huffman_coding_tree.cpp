#include <iostream>
#include <queue>
#include <string>
#include <map>

struct MinHeapNode {
    char data;
    unsigned freq;
    MinHeapNode *left, *right;
    MinHeapNode(char data, unsigned freq) : data(data), freq(freq), left(nullptr), right(nullptr) {}
};

struct compare {
    bool operator()(MinHeapNode* l, MinHeapNode* r) { return l->freq > r->freq; }
};

void print_codes(MinHeapNode* root, std::string str) {
    if (!root) return;
    if (root->data != '$') std::cout << root->data << ": " << str << "\n";
    print_codes(root->left, str + "0");
    print_codes(root->right, str + "1");
}

int main() {
    std::priority_queue<MinHeapNode*, std::vector<MinHeapNode*>, compare> min_heap;
    min_heap.push(new MinHeapNode('a', 5));
    min_heap.push(new MinHeapNode('b', 9));
    min_heap.push(new MinHeapNode('c', 12));
    min_heap.push(new MinHeapNode('d', 13));
    min_heap.push(new MinHeapNode('e', 16));
    min_heap.push(new MinHeapNode('f', 45));

    while (min_heap.size() != 1) {
        auto *left = min_heap.top(); min_heap.pop();
        auto *right = min_heap.top(); min_heap.pop();
        auto *top = new MinHeapNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;
        min_heap.push(top);
    }

    std::cout << "Huffman Codes:\n";
    print_codes(min_heap.top(), "");
    return 0;
}
