"""BST: Kth Smallest Element in BST (Inorder Traversal)."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode | None, k: int) -> int:
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

    return -1

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print("1st smallest:", kth_smallest(root, 1))
    print("3rd smallest:", kth_smallest(root, 3))
