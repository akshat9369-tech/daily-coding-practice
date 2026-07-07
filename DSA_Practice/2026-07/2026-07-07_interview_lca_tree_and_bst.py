"""Lowest Common Ancestor of Binary Tree and BST."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def lca_bst(root: TreeNode | None, p: int, q: int) -> TreeNode | None:
    curr = root
    while curr:
        if p < curr.val and q < curr.val:
            curr = curr.left
        elif p > curr.val and q > curr.val:
            curr = curr.right
        else:
            return curr
    return None

if __name__ == "__main__":
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    ans = lca_bst(root, 2, 8)
    print("LCA in BST of 2 and 8:", ans.val if ans else None)
    ans2 = lca_bst(root, 2, 4)
    print("LCA in BST of 2 and 4:", ans2.val if ans2 else None)
