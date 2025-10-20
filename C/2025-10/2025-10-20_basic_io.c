#include <stdio.h>

int main(void) {
    int age = 21;
    float gpa = 3.85f;
    char grade = 'A';

    printf("Student Details:\n");
    printf("Age   : %d years\n", age);
    printf("GPA   : %.2f\n", gpa);
    printf("Grade : %c\n", grade);

    return 0;
}
