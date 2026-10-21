"""Linked List: Palindrome Linked List Check in O(1) Space."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def is_palindrome_list(head: ListNode | None) -> bool:
    if not head or not head.next:
        return True

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    p1, p2 = head, prev
    while p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

if __name__ == "__main__":
    pal = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print("Is Palindrome:", is_palindrome_list(pal))
