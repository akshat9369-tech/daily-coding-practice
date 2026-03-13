"""Linked List: Detect Cycle and Cycle Starting Node (Floyd's)."""

class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None

def detect_cycle_start(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    entry = head
    while entry != slow:
        entry = entry.next
        slow = slow.next

    return entry

if __name__ == "__main__":
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2  # Cycle back to n2

    cycle_node = detect_cycle_start(n1)
    print("Cycle starts at node value:", cycle_node.val if cycle_node else "No Cycle")
