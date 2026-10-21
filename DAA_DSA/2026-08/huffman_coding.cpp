#include <iostream>
#include <queue>
#include <map>
#include <string>

struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(Node* a, Node* b) { return a->freq > b->freq; }
};

void encode(Node* root, std::string str, std::map<char, std::string>& huffmanCode) {
    if (!root) return;
    if (!root->left && !root->right) huffmanCode[root->ch] = str;
    encode(root->left, str + "0", huffmanCode);
    encode(root->right, str + "1", huffmanCode);
}

int main() {
    std::string text = "huffman_coding_implementation";
    std::map<char, int> freq;
    for (char c : text) freq[c]++;

    std::priority_queue<Node*, std::vector<Node*>, Compare> pq;
    for (auto pair : freq) pq.push(new Node(pair.first, pair.second));

    while (pq.size() != 1) {
        Node* l = pq.top(); pq.pop();
        Node* r = pq.top(); pq.pop();
        Node* sum = new Node('\0', l->freq + r->freq);
        sum->left = l; sum->right = r;
        pq.push(sum);
    }

    std::map<char, std::string> huffmanCode;
    encode(pq.top(), "", huffmanCode);

    std::cout << "Huffman Codes for characters in '" << text << "':\n";
    for (auto p : huffmanCode) std::cout << p.first << ": " << p.second << "\n";
    return 0;
}
