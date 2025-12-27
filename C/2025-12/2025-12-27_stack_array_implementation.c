#include <stdio.h>
#include <stdbool.h>

#define CAPACITY 5

typedef struct {
    int items[CAPACITY];
    int top;
} Stack;

void init_stack(Stack *s) { s->top = -1; }
bool is_empty(Stack *s) { return s->top == -1; }
bool is_full(Stack *s) { return s->top == CAPACITY - 1; }

bool push(Stack *s, int val) {
    if (is_full(s)) return false;
    s->items[++(s->top)] = val;
    return true;
}

bool pop(Stack *s, int *out) {
    if (is_empty(s)) return false;
    *out = s->items[(s->top)--];
    return true;
}

int main(void) {
    Stack s;
    init_stack(&s);

    push(&s, 10); push(&s, 20); push(&s, 30);
    printf("Pushed 10, 20, 30\n");

    int val;
    while (pop(&s, &val)) {
        printf("Popped: %d\n", val);
    }
    return 0;
}
