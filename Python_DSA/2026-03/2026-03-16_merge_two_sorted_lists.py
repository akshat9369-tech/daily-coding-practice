"""Linked List: Merge Two Sorted Linked Lists."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

def to_list(head: ListNode | None) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    merged = merge_two_lists(l1, l2)
    print("Merged List:", to_list(merged))
