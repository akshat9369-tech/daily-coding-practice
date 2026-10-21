"""Nested Data Structures and Deep vs Shallow Copying."""

import copy

def demonstrate_copies():
    original = {
        "group": "Alpha",
        "members": [{"id": 1, "name": "Akshat"}, {"id": 2, "name": "Bob"}],
        "metrics": [10, 20, 30]
    }

    shallow = original.copy()
    deep = copy.deepcopy(original)

    # Mutate nested object
    original["members"][0]["name"] = "Alice"
    original["metrics"].append(40)

    print("After mutating original nested list:")
    print(f"Original members[0]: {original['members'][0]['name']}")
    print(f"Shallow  members[0]: {shallow['members'][0]['name']} (reflects mutation!)")
    print(f"Deep     members[0]: {deep['members'][0]['name']} (isolated deep copy!)")

if __name__ == "__main__":
    demonstrate_copies()
