"""Graph: Cycle Detection in Directed Graph (DFS Recursion Stack)."""

def has_cycle_directed(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj = {i: [] for i in range(num_courses)}
    for u, v in prerequisites:
        adj[u].append(v)

    visited = [0] * num_courses  # 0: unvisited, 1: visiting, 2: visited

    def dfs(u: int) -> bool:
        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 1:
                return True
            if visited[v] == 0 and dfs(v):
                return True
        visited[u] = 2
        return False

    for i in range(num_courses):
        if visited[i] == 0:
            if dfs(i):
                return True
    return False

if __name__ == "__main__":
    cycle_graph = [[0, 1], [1, 2], [2, 0]]
    dag = [[0, 1], [1, 2], [0, 2]]
    print("Directed cycle present:", has_cycle_directed(3, cycle_graph))
    print("DAG cycle present     :", has_cycle_directed(3, dag))
