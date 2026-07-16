"""Alien Dictionary (Topological Sort on Character Graph)."""

from collections import defaultdict, Counter, deque

def alien_order(words: list[str]) -> str:
    adj = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})

    for first, second in zip(words, words[1:]):
        if len(first) > len(second) and first.startswith(second):
            return ""  # Invalid prefix condition
        for c1, c2 in zip(first, second):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    in_degree[c2] += 1
                break

    q = deque([c for c in in_degree if in_degree[c] == 0])
    order = []

    while q:
        c = q.popleft()
        order.append(c)
        for nbr in adj[c]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                q.append(nbr)

    return "".join(order) if len(order) == len(in_degree) else ""

if __name__ == "__main__":
    alien_words = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Alien Dictionary alphabet order:", alien_order(alien_words))
