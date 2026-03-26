"""Binary Tree: Lowest Common Ancestor (LCA)."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

if __name__ == "__main__":
    p = TreeNode(5, TreeNode(6), TreeNode(2))
    q = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, p, q)
    lca = lowest_common_ancestor(root, p, q)
    print("LCA value:", lca.val if lca else "None")
