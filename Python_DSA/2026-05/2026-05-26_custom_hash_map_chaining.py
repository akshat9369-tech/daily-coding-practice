"""Hashing: Custom Hash Map Implementation with Chaining."""

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx] = [(k, v) for k, v in self.buckets[idx] if k != key]

if __name__ == "__main__":
    hm = MyHashMap()
    hm.put(1, 100)
    hm.put(2, 200)
    print("Get 1:", hm.get(1))
    print("Get 3:", hm.get(3))
    hm.put(2, 250)
    print("Get 2 (updated):", hm.get(2))
    hm.remove(2)
    print("Get 2 (removed):", hm.get(2))
