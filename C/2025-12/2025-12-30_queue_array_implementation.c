#include <stdio.h>
#include <stdbool.h>

#define MAX 5

typedef struct {
    int data[MAX];
    int front;
    int rear;
} LinearQueue;

void init_queue(LinearQueue *q) { q->front = 0; q->rear = -1; }

bool enqueue(LinearQueue *q, int val) {
    if (q->rear == MAX - 1) return false;
    q->data[++(q->rear)] = val;
    return true;
}

bool dequeue(LinearQueue *q, int *out) {
    if (q->front > q->rear) return false;
    *out = q->data[(q->front)++];
    return true;
}

int main(void) {
    LinearQueue q;
    init_queue(&q);

    enqueue(&q, 1); enqueue(&q, 2); enqueue(&q, 3);

    int val;
    while (dequeue(&q, &val)) {
        printf("Dequeued: %d\n", val);
    }
    return 0;
}
