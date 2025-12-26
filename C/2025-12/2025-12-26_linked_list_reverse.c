#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *reverse_list(struct Node *head) {
    struct Node *prev = NULL;
    struct Node *curr = head;
    struct Node *next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

void push(struct Node **head, int val) {
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->data = val;
    node->next = *head;
    *head = node;
}

void print_nodes(struct Node *head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main(void) {
    struct Node *head = NULL;
    for (int i = 5; i >= 1; i--) push(&head, i * 10);

    printf("Original: "); print_nodes(head);
    head = reverse_list(head);
    printf("Reversed: "); print_nodes(head);
    return 0;
}
