#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::string get_lcs(const std::string& X, const std::string& Y) {
    int m = X.length(), n = Y.length();
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    int i = m, j = n;
    std::string lcs_str = "";
    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcs_str.push_back(X[i - 1]);
            i--; j--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) i--;
        else j--;
    }
    std::reverse(lcs_str.begin(), lcs_str.end());
    return lcs_str;
}

int main() {
    std::string s1 = "AGGTAB", s2 = "GXTXAYB";
    std::cout << "LCS of " << s1 << " and " << s2 << ": " << get_lcs(s1, s2) << std::endl;
    return 0;
}
