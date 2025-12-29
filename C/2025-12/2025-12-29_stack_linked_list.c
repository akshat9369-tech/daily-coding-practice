#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct StackNode {
    int data;
    struct StackNode *next;
};

typedef struct {
    struct StackNode *top;
    int size;
} LinkedListStack;

void init(LinkedListStack *s) { s->top = NULL; s->size = 0; }

void push(LinkedListStack *s, int val) {
    struct StackNode *node = (struct StackNode *)malloc(sizeof(struct StackNode));
    node->data = val;
    node->next = s->top;
    s->top = node;
    s->size++;
}

bool pop(LinkedListStack *s, int *val) {
    if (!s->top) return false;
    struct StackNode *temp = s->top;
    *val = temp->data;
    s->top = temp->next;
    free(temp);
    s->size--;
    return true;
}

int main(void) {
    LinkedListStack s;
    init(&s);

    push(&s, 100); push(&s, 200); push(&s, 300);
    printf("Stack size: %d\n", s.size);

    int val;
    while (pop(&s, &val)) {
        printf("Popped: %d\n", val);
    }
    return 0;
}
