#include <stdio.h>
#include <ctype.h>

void analyze_string(const char *str, int *vowels, int *consonants, int *digits, int *spaces) {
    *vowels = 0;
    *consonants = 0;
    *digits = 0;
    *spaces = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        char ch = str[i];
        if (isalpha((unsigned char)ch)) {
            char lower = tolower((unsigned char)ch);
            if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
                (*vowels)++;
            } else {
                (*consonants)++;
            }
        } else if (isdigit((unsigned char)ch)) {
            (*digits)++;
        } else if (isspace((unsigned char)ch)) {
            (*spaces)++;
        }
    }
}

int main(void) {
    const char *text = "C Programming 2025: Master Algorithms & Data Structures!";
    int v, c, d, s;
    analyze_string(text, &v, &c, &d, &s);

    printf("Analysis for: \"%s\"\n", text);
    printf("Vowels: %d | Consonants: %d | Digits: %d | Spaces: %d\n", v, c, d, s);
    return 0;
}
