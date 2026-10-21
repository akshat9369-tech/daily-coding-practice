"""Graph: Adjacency List and Adjacency Matrix Representations."""

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1, directed: bool = False):
        self.adj_list[u].append((v, weight))
        self.adj_matrix[u][v] = weight
        if not directed:
            self.adj_list[v].append((u, weight))
            self.adj_matrix[v][u] = weight

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    print("Adjacency List:")
    for node, neighbors in g.adj_list.items():
        print(f"  {node} -> {neighbors}")
