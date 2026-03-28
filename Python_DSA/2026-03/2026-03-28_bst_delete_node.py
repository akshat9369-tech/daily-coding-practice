"""BST: Delete Node in Binary Search Tree."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def delete_node(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Find inorder successor (min in right subtree)
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete_node(root.right, succ.val)

    return root

def inorder(root: TreeNode | None) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    print("Before deletion:", inorder(root))
    root = delete_node(root, 3)
    print("After deleting 3:", inorder(root))
