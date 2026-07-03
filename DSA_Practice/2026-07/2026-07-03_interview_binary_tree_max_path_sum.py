"""Binary Tree Maximum Path Sum."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode | None) -> int:
    max_sum = float("-inf")

    def max_gain(node: TreeNode | None) -> int:
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        current_path = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path)

        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum

if __name__ == "__main__":
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Max Path Sum:", max_path_sum(root))
