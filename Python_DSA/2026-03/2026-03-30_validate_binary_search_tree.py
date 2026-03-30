"""BST: Validate Binary Search Tree (IsValidBST)."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode | None) -> bool:
    def validate(node: TreeNode | None, low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    valid_bst = TreeNode(2, TreeNode(1), TreeNode(3))
    print("Valid BST:", is_valid_bst(valid_bst))

    invalid_bst = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print("Invalid BST:", is_valid_bst(invalid_bst))
