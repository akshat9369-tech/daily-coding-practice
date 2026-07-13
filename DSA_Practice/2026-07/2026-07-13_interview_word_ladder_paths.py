"""Word Ladder I and II (Shortest Sequence and All Paths)."""

from collections import defaultdict, deque

def find_ladders(begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:
    words = set(word_list)
    if end_word not in words:
        return []

    level = {begin_word: [[begin_word]]}

    while level:
        next_level = defaultdict(list)
        for word in level:
            if word == end_word:
                return level[word]
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + c + word[i + 1:]
                    if nxt in words:
                        for path in level[word]:
                            next_level[nxt].append(path + [nxt])
        words -= set(next_level.keys())
        level = next_level

    return []

if __name__ == "__main__":
    res = find_ladders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print("All shortest paths for word ladder:")
    for p in res:
        print(" ", " -> ".join(p))
