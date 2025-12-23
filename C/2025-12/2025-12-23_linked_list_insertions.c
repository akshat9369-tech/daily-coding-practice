#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node *next;
};

void insert_head(struct Node **head, int val) {
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->val = val;
    node->next = *head;
    *head = node;
}

void insert_tail(struct Node **head, int val) {
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->val = val;
    node->next = NULL;
    if (*head == NULL) {
        *head = node;
        return;
    }
    struct Node *curr = *head;
    while (curr->next) curr = curr->next;
    curr->next = node;
}

void print_all(struct Node *head) {
    while (head) {
        printf("%d -> ", head->val);
        head = head->next;
    }
    printf("NULL\n");
}

void cleanup(struct Node *head) {
    while (head) {
        struct Node *t = head;
        head = head->next;
        free(t);
    }
}

int main(void) {
    struct Node *head = NULL;
    insert_tail(&head, 20);
    insert_tail(&head, 30);
    insert_head(&head, 10);
    insert_tail(&head, 40);

    print_all(head);
    cleanup(head);
    return 0;
}
