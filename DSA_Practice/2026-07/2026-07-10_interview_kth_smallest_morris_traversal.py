"""Kth Smallest Element in BST with Morris Inorder Traversal."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_morris(root: TreeNode | None, k: int) -> int:
    curr = root
    ans = -1

    while curr:
        if not curr.left:
            k -= 1
            if k == 0:
                ans = curr.val
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                k -= 1
                if k == 0:
                    ans = curr.val
                curr = curr.right

    return ans

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print("2nd smallest (Morris):", kth_smallest_morris(root, 2))
