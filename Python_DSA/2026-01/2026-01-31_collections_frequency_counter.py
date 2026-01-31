"""Frequency Counting and Collections (Counter, defaultdict)."""

from collections import Counter, defaultdict

def demonstrate_frequency_counting():
    sentence = "the quick brown fox jumps over the lazy dog jumps over the fence"
    words = sentence.split()

    # Counter
    freq_counter = Counter(words)
    print("Top 3 most frequent words:")
    for word, count in freq_counter.most_common(3):
        print(f"  {word:6s} -> {count} times")

    # Grouping by length using defaultdict
    grouped_by_len = defaultdict(list)
    for w in set(words):
        grouped_by_len[len(w)].append(w)

    print("\nWords grouped by length:")
    for length in sorted(grouped_by_len):
        print(f"  Length {length}: {grouped_by_len[length]}")

if __name__ == "__main__":
    demonstrate_frequency_counting()
