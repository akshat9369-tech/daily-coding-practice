"""Linked List: Remove Nth Node from End of List."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next

def to_list(head: ListNode | None) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original:", to_list(head))
    head = remove_nth_from_end(head, 2)
    print("After removing 2nd from end:", to_list(head))
