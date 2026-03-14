"""Linked List: Find Middle Node (Fast and Slow Pointer)."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def middle_node(head: ListNode | None) -> ListNode | None:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    mid = middle_node(head)
    print("Middle node value:", mid.val if mid else "None")
