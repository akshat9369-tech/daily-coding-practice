#include <stdio.h>
#include <stdbool.h>

#define SIZE 5

typedef struct {
    int items[SIZE];
    int front;
    int rear;
    int count;
} CircularQueue;

void init_cqueue(CircularQueue *q) {
    q->front = 0;
    q->rear = -1;
    q->count = 0;
}

bool is_full(CircularQueue *q) { return q->count == SIZE; }
bool is_empty(CircularQueue *q) { return q->count == 0; }

bool enqueue(CircularQueue *q, int value) {
    if (is_full(q)) return false;
    q->rear = (q->rear + 1) % SIZE;
    q->items[q->rear] = value;
    q->count++;
    return true;
}

bool dequeue(CircularQueue *q, int *out) {
    if (is_empty(q)) return false;
    *out = q->items[q->front];
    q->front = (q->front + 1) % SIZE;
    q->count--;
    return true;
}

int main(void) {
    CircularQueue q;
    init_cqueue(&q);

    for (int i = 1; i <= 5; i++) enqueue(&q, i * 10);
    printf("Queue is full: %s\n", is_full(&q) ? "YES" : "NO");

    int val;
    dequeue(&q, &val);
    printf("Dequeued %d, adding 60\n", val);
    enqueue(&q, 60);

    while (dequeue(&q, &val)) {
        printf("Dequeued: %d\n", val);
    }
    return 0;
}
