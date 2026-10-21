"""Queue: Circular Queue Implementation."""

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.head = 0
        self.count = 0

    def en_queue(self, value: int) -> bool:
        if self.is_full():
            return False
        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def de_queue(self) -> bool:
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self.queue[self.head]

    def rear(self) -> int:
        if self.is_empty():
            return -1
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity

if __name__ == "__main__":
    cq = MyCircularQueue(3)
    print(cq.en_queue(1))
    print(cq.en_queue(2))
    print(cq.en_queue(3))
    print("Full:", cq.is_full())
    print("Front:", cq.front(), "Rear:", cq.rear())
    cq.de_queue()
    cq.en_queue(4)
    print("New Rear:", cq.rear())
