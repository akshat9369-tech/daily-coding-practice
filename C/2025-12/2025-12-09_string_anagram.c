#include <stdio.h>
#include <ctype.h>

int are_anagrams(const char *s1, const char *s2) {
    int freq[26] = {0};

    for (int i = 0; s1[i] != '\0'; i++) {
        if (isalpha((unsigned char)s1[i])) {
            freq[tolower((unsigned char)s1[i]) - 'a']++;
        }
    }
    for (int i = 0; s2[i] != '\0'; i++) {
        if (isalpha((unsigned char)s2[i])) {
            freq[tolower((unsigned char)s2[i]) - 'a']--;
        }
    }
    for (int i = 0; i < 26; i++) {
        if (freq[i] != 0) return 0;
    }
    return 1;
}

int main(void) {
    printf("silent / listen : %s\n", are_anagrams("silent", "listen") ? "ANAGRAM" : "NO");
    printf("triangle / integral : %s\n", are_anagrams("triangle", "integral") ? "ANAGRAM" : "NO");
    printf("apple / pale : %s\n", are_anagrams("apple", "pale") ? "ANAGRAM" : "NO");
    return 0;
}
