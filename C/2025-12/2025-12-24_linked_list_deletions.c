#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void append(struct Node **head, int data) {
    struct Node *n = (struct Node *)malloc(sizeof(struct Node));
    n->data = data;
    n->next = NULL;
    if (!*head) { *head = n; return; }
    struct Node *c = *head;
    while (c->next) c = c->next;
    c->next = n;
}

int delete_value(struct Node **head, int key) {
    struct Node *curr = *head, *prev = NULL;
    if (curr && curr->data == key) {
        *head = curr->next;
        free(curr);
        return 1;
    }
    while (curr && curr->data != key) {
        prev = curr;
        curr = curr->next;
    }
    if (!curr) return 0;
    prev->next = curr->next;
    free(curr);
    return 1;
}

void display_list(struct Node *head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main(void) {
    struct Node *head = NULL;
    append(&head, 10); append(&head, 20); append(&head, 30); append(&head, 40);

    printf("Before deletion: "); display_list(head);
    delete_value(&head, 20);
    printf("After deleting 20: "); display_list(head);
    delete_value(&head, 10);
    printf("After deleting 10: "); display_list(head);
    return 0;
}
