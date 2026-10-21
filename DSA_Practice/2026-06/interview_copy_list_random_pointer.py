"""Copy List with Random Pointer (O(1) Space Interleaving)."""

class Node:
    def __init__(self, val: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head: Node | None) -> Node | None:
    if not head:
        return None

    # Step 1: Interleave cloned nodes
    curr = head
    while curr:
        copy = Node(curr.val, curr.next)
        curr.next = copy
        curr = copy.next

    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate lists
    curr = head
    copy_head = head.next
    while curr:
        copy = curr.next
        curr.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        curr = curr.next

    return copy_head

if __name__ == "__main__":
    n1, n2 = Node(1), Node(2)
    n1.next = n2
    n1.random = n2
    n2.random = n2

    cloned = copy_random_list(n1)
    print("Cloned head val:", cloned.val if cloned else None)
    print("Cloned random val:", cloned.random.val if cloned and cloned.random else None)
