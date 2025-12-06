#include <stdio.h>
#include <ctype.h>

int is_palindrome_string(const char *str) {
    int left = 0, right = 0;
    while (str[right] != '\0') right++;
    right--;

    while (left < right) {
        while (left < right && !isalnum((unsigned char)str[left])) left++;
        while (left < right && !isalnum((unsigned char)str[right])) right--;
        if (tolower((unsigned char)str[left]) != tolower((unsigned char)str[right])) {
            return 0;
        }
        left++;
        right--;
    }
    return 1;
}

int main(void) {
    const char *samples[] = {"racecar", "A man a plan a canal Panama", "hello", "Was it a car or a cat I saw"};
    for (int i = 0; i < 4; i++) {
        printf("\"%s\" -> %s\n", samples[i],
               is_palindrome_string(samples[i]) ? "PALINDROME" : "NOT A PALINDROME");
    }
    return 0;
}
