"""Construct Binary Tree from Preorder and Inorder Traversal."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    inorder_idx = {val: i for i, val in enumerate(inorder)}
    pre_iter = iter(preorder)

    def helper(left: int, right: int) -> TreeNode | None:
        if left > right:
            return None
        root_val = next(pre_iter)
        root = TreeNode(root_val)
        mid = inorder_idx[root_val]

        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(inorder) - 1)

def level_order(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    res = []
    q = [root]
    while q:
        curr = q.pop(0)
        res.append(curr.val)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return res

if __name__ == "__main__":
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    tree = build_tree(pre, ino)
    print("Constructed tree level order:", level_order(tree))
