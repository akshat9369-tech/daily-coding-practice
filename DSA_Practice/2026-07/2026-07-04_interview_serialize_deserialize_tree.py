"""Serialize and Deserialize Binary Tree (Preorder and BFS)."""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        vals = []
        def dfs(node: TreeNode | None):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode | None:
        vals = iter(data.split(","))
        def dfs() -> TreeNode | None:
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = codec.serialize(root)
    print("Serialized:", serialized)
    restored = codec.deserialize(serialized)
    print("Restored root:", restored.val, "left:", restored.left.val, "right:", restored.right.val)
