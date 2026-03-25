"""Binary Tree: Symmetric Tree Check."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode | None) -> bool:
    if not root:
        return True

    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    return is_mirror(root.left, root.right)

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print("Is symmetric:", is_symmetric(root))
