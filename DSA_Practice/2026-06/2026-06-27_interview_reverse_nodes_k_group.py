"""Reverse Nodes in k-Group (Hard Linked List)."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def reverse_k_group(head: ListNode | None, k: int) -> ListNode | None:
    dummy = ListNode(0, head)
    group_prev = dummy

    def get_kth(curr: ListNode | None, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        # Reverse group
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next

def to_list(head: ListNode | None) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Reversed in k=2 groups:", to_list(reverse_k_group(nodes, 2)))
