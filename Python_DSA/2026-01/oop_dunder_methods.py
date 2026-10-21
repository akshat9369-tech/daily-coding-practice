"""OOP: Dunder Magic Methods (__str__, __repr__, __len__, __getitem__)."""

class CustomVector:
    def __init__(self, *components: float):
        self.components = list(components)

    def __len__(self) -> int:
        return len(self.components)

    def __getitem__(self, index: int) -> float:
        return self.components[index]

    def __add__(self, other: "CustomVector") -> "CustomVector":
        if len(self) != len(other):
            raise ValueError("Vectors must be of identical dimension to add.")
        return CustomVector(*(a + b for a, b in zip(self.components, other.components)))

    def __repr__(self) -> str:
        return f"CustomVector({', '.join(map(str, self.components))})"

    def __str__(self) -> str:
        return f"Vector<{', '.join(map(str, self.components))}>"

if __name__ == "__main__":
    v1 = CustomVector(1.0, 2.0, 3.0)
    v2 = CustomVector(4.0, 5.0, 6.0)
    v3 = v1 + v2

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v3)
    print("v3 length:", len(v3))
    print("v3[1]:", v3[1])
