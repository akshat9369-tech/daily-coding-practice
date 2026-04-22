"""All-Pairs Shortest Path: Floyd-Warshall Algorithm."""

def floyd_warshall(graph: list[list[float]]) -> list[list[float]]:
    v = len(graph)
    dist = [row.copy() for row in graph]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

if __name__ == "__main__":
    INF = float("inf")
    g = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    all_pairs = floyd_warshall(g)
    print("Floyd-Warshall all-pairs distance matrix:")
    for row in all_pairs:
        print(" ", row)
