"""Graph: Course Schedule I and II (Prerequisites Resolution)."""

from collections import deque

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses

    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1

    q = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while q:
        course = q.popleft()
        order.append(course)
        for nbr in adj[course]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                q.append(nbr)

    return order if len(order) == num_courses else []

if __name__ == "__main__":
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print("Course Schedule Order:", find_order(4, prereqs))
