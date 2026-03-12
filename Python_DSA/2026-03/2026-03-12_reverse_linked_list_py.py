"""Linked List: Reverse Singly Linked List (Iterative and Recursive)."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def reverse_list_iterative(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def to_list(head: ListNode | None) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original:", to_list(head))
    rev = reverse_list_iterative(head)
    print("Reversed:", to_list(rev))
