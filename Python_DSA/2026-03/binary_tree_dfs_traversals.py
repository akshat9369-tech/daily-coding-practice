"""Binary Tree: Node Class and Depth-First Traversals."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root: TreeNode | None) -> list[int]:
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root: TreeNode | None) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def postorder(root: TreeNode | None) -> list[int]:
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

if __name__ == "__main__":
    # Tree:   1
    #        /     #       2   3
    #      /     #     4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Preorder :", preorder(root))
    print("Inorder  :", inorder(root))
    print("Postorder:", postorder(root))
