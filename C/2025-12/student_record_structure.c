#include <stdio.h>
#include <string.h>

struct Student {
    int id;
    char name[32];
    float marks;
};

void display_student(const struct Student *s) {
    printf("ID: %4d | Name: %-12s | Marks: %.2f\n", s->id, s->name, s->marks);
}

int main(void) {
    struct Student s1;
    s1.id = 101;
    strncpy(s1.name, "Akshat", sizeof(s1.name) - 1);
    s1.name[sizeof(s1.name) - 1] = '\0';
    s1.marks = 92.5f;

    struct Student s2 = {102, "Bob", 88.0f};

    display_student(&s1);
    display_student(&s2);
    return 0;
}
