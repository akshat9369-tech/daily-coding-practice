"""Binary Tree: Level Order Traversal (BFS with Queue)."""

from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(current_level)

    return result

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Level order:", level_order(root))
