"""Graph: Word Ladder Shortest Transformation (Bidirectional BFS)."""

from collections import deque

def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end_word not in words:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps

        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + ch + word[i + 1:]
                if next_word in words and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0

if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    bank = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("Shortest transformation length:", ladder_length(begin, end, bank))
