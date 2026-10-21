#include <iostream>
#include <string>
#include <vector>

void rabin_karp(const std::string& pat, const std::string& txt, int q = 101) {
    int d = 256;
    int M = pat.length(), N = txt.length();
    int p = 0, t = 0, h = 1;

    for (int i = 0; i < M - 1; i++) h = (h * d) % q;

    for (int i = 0; i < M; i++) {
        p = (d * p + pat[i]) % q;
        t = (d * t + txt[i]) % q;
    }

    std::cout << "Rabin-Karp matches: ";
    for (int i = 0; i <= N - M; i++) {
        if (p == t) {
            bool match = true;
            for (int j = 0; j < M; j++) if (txt[i + j] != pat[j]) { match = false; break; }
            if (match) std::cout << i << " ";
        }
        if (i < N - M) {
            t = (d * (t - txt[i] * h) + txt[i + M]) % q;
            if (t < 0) t += q;
        }
    }
    std::cout << std::endl;
}

int main() {
    rabin_karp("GEEK", "GEEKS FOR GEEKS");
    return 0;
}
