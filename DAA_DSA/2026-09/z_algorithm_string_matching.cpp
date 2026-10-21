#include <iostream>
#include <vector>
#include <string>

std::vector<int> compute_z(const std::string& s) {
    int n = s.length();
    std::vector<int> Z(n, 0);
    int L = 0, R = 0;
    for (int i = 1; i < n; i++) {
        if (i > R) {
            L = R = i;
            while (R < n && s[R - L] == s[R]) R++;
            Z[i] = R - L; R--;
        } else {
            int k = i - L;
            if (Z[k] < R - i + 1) Z[i] = Z[k];
            else {
                L = i;
                while (R < n && s[R - L] == s[R]) R++;
                Z[i] = R - L; R--;
            }
        }
    }
    return Z;
}

int main() {
    std::string txt = "baabaa", pat = "aab";
    std::string concat = pat + "$" + txt;
    auto Z = compute_z(concat);
    std::cout << "Z-Algorithm matches: ";
    for (size_t i = 0; i < Z.size(); i++) {
        if (Z[i] == (int)pat.length()) std::cout << (i - pat.length() - 1) << " ";
    }
    std::cout << std::endl;
    return 0;
}
