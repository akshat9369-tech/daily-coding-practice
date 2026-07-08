"""All Nodes Distance K in Binary Tree (Graph Mapping)."""

from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def distance_k(root: TreeNode | None, target: TreeNode, k: int) -> list[int]:
    parents = {}
    def build_parents(node: TreeNode | None, parent: TreeNode | None):
        if not node:
            return
        parents[node] = parent
        build_parents(node.left, node)
        build_parents(node.right, node)

    build_parents(root, None)

    queue = deque([(target, 0)])
    visited = {target}

    while queue:
        if queue[0][1] == k:
            return [node.val for node, _ in queue]
        node, dist = queue.popleft()
        for neighbor in (node.left, node.right, parents[node]):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return []

if __name__ == "__main__":
    t = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, t, TreeNode(1, TreeNode(0), TreeNode(8)))
    print("Nodes distance 2 from target 5:", distance_k(root, t, 2))
