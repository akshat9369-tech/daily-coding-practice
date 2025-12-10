#include <stdio.h>

int main(void) {
    int value = 42;
    int *ptr = &value;

    printf("Value of variable       : %d\n", value);
    printf("Address of variable (&) : %p\n", (void*)&value);
    printf("Value of pointer (ptr)  : %p\n", (void*)ptr);
    printf("Dereference pointer (*) : %d\n", *ptr);

    *ptr = 100;
    printf("After mutating via ptr  : %d\n", value);

    return 0;
}
