"""Trie: Word Dictionary with Wildcard Search."""

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordDictionary()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j: int, root: WordDictionary) -> bool:
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_word

        return dfs(0, self)

if __name__ == "__main__":
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    print("Search 'pad':", wd.search("pad"))
    print("Search 'bad':", wd.search("bad"))
    print("Search '.ad':", wd.search(".ad"))
    print("Search 'b..':", wd.search("b.."))
