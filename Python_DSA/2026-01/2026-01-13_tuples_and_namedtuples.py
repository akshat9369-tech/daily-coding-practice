"""Tuples, Immutability, and NamedTuples."""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "label"])

def tuple_fundamentals():
    coords = (10, 20, 30)
    x, y, z = coords
    print(f"Unpacked 3D coords: x={x}, y={y}, z={z}")

    p1 = Point(4.5, 7.8, "Station_A")
    p2 = Point(1.2, 3.4, "Station_B")

    distance = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Euclidean distance: {distance:.3f}")

if __name__ == "__main__":
    tuple_fundamentals()
