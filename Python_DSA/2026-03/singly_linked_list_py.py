"""Linked List: Singly Linked List Implementation."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val: int):
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def to_list(self) -> list[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

if __name__ == "__main__":
    sll = SinglyLinkedList()
    for v in [10, 20, 30, 40]:
        sll.append(v)
    print("Singly Linked List:", sll.to_list())
