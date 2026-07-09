"""Validate and Recover Binary Search Tree."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def recover_tree(root: TreeNode | None) -> None:
    first = second = prev = None

    def inorder(node: TreeNode | None):
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)
        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    if first and second:
        first.val, second.val = second.val, first.val

def to_inorder(root: TreeNode | None) -> list[int]:
    return to_inorder(root.left) + [root.val] + to_inorder(root.right) if root else []

if __name__ == "__main__":
    # Swapped 1 and 3
    root = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
    print("Before recovery:", to_inorder(root))
    recover_tree(root)
    print("After recovery :", to_inorder(root))
