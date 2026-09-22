#include <iostream>
#include <vector>
#include <string>

std::vector<int> compute_lps(const std::string& pat) {
    int m = pat.length();
    std::vector<int> lps(m, 0);
    int len = 0, i = 1;
    while (i < m) {
        if (pat[i] == pat[len]) {
            len++;
            lps[i++] = len;
        } else {
            if (len != 0) len = lps[len - 1];
            else lps[i++] = 0;
        }
    }
    return lps;
}

void kmp_search(const std::string& pat, const std::string& txt) {
    int m = pat.length(), n = txt.length();
    std::vector<int> lps = compute_lps(pat);
    int i = 0, j = 0;
    std::cout << "KMP Match indices: ";
    while (i < n) {
        if (pat[j] == txt[i]) { i++; j++; }
        if (j == m) {
            std::cout << (i - j) << " ";
            j = lps[j - 1];
        } else if (i < n && pat[j] != txt[i]) {
            if (j != 0) j = lps[j - 1];
            else i++;
        }
    }
    std::cout << std::endl;
}

int main() {
    kmp_search("ABABCABAB", "ABABDABACDABABCABAB");
    return 0;
}
