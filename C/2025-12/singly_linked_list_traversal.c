#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *create_node(int value) {
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    if (node) {
        node->data = value;
        node->next = NULL;
    }
    return node;
}

void print_list(const struct Node *head) {
    const struct Node *curr = head;
    while (curr != NULL) {
        printf("%d -> ", curr->data);
        curr = curr->next;
    }
    printf("NULL\n");
}

void free_list(struct Node *head) {
    while (head) {
        struct Node *temp = head;
        head = head->next;
        free(temp);
    }
}

int main(void) {
    struct Node *head = create_node(10);
    head->next = create_node(20);
    head->next->next = create_node(30);

    print_list(head);
    free_list(head);
    return 0;
}
