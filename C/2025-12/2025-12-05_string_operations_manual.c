#include <stdio.h>

int my_strlen(const char *str) {
    int len = 0;
    while (str[len] != '\0') len++;
    return len;
}

void my_strcpy(char *dest, const char *src) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

void my_strcat(char *dest, const char *src) {
    int dest_len = my_strlen(dest);
    int i = 0;
    while (src[i] != '\0') {
        dest[dest_len + i] = src[i];
        i++;
    }
    dest[dest_len + i] = '\0';
}

int main(void) {
    char buffer[64];
    my_strcpy(buffer, "Hello");
    printf("Length of buffer: %d\n", my_strlen(buffer));

    my_strcat(buffer, ", World!");
    printf("Concatenated: %s (len: %d)\n", buffer, my_strlen(buffer));
    return 0;
}
