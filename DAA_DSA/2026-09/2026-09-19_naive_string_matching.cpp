#include <iostream>
#include <string>
#include <vector>

std::vector<int> naive_search(const std::string& pat, const std::string& txt) {
    std::vector<int> positions;
    int M = pat.length(), N = txt.length();
    for (int i = 0; i <= N - M; i++) {
        int j = 0;
        while (j < M && txt[i + j] == pat[j]) j++;
        if (j == M) positions.push_back(i);
    }
    return positions;
}

int main() {
    std::string txt = "AABAACAADAABAABA", pat = "AABA";
    auto res = naive_search(pat, txt);
    std::cout << "Pattern found at indices: ";
    for (int idx : res) std::cout << idx << " ";
    std::cout << std::endl;
    return 0;
}
