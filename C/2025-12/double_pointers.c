#include <stdio.h>

void allocate_and_set(int **pptr, int val) {
    static int storage;
    storage = val;
    *pptr = &storage;
}

int main(void) {
    int a = 10;
    int *p = &a;
    int **pp = &p;

    printf("Direct a: %d | Single pointer *p: %d | Double pointer **pp: %d\n", a, *p, **pp);

    int *new_ptr = NULL;
    allocate_and_set(&new_ptr, 777);
    printf("Target assigned via double pointer: %d\n", *new_ptr);
    return 0;
}
