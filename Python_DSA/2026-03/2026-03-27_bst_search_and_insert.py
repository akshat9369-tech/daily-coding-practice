"""BST: Search and Insert in Binary Search Tree."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root: TreeNode | None, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def search_bst(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)

def inorder(root: TreeNode | None) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

if __name__ == "__main__":
    root = None
    for v in [4, 2, 7, 1, 3]:
        root = insert_into_bst(root, v)

    print("BST Inorder:", inorder(root))
    found = search_bst(root, 2)
    print("Found 2:", found is not None)
