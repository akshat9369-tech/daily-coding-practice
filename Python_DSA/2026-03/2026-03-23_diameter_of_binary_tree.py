"""Binary Tree: Diameter of Binary Tree."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode | None) -> int:
    max_diameter = 0

    def depth(node: TreeNode | None) -> int:
        nonlocal max_diameter
        if not node:
            return 0
        left_h = depth(node.left)
        right_h = depth(node.right)
        max_diameter = max(max_diameter, left_h + right_h)
        return 1 + max(left_h, right_h)

    depth(root)
    return max_diameter

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Diameter of binary tree:", diameter_of_binary_tree(root))
