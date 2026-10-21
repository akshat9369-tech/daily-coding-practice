"""Lists: In-Depth Operations, Slicing, and Sorting."""

def demonstrate_list_methods():
    nums = [40, 10, 20, 50, 30]

    nums.append(60)
    nums.extend([70, 80])
    nums.insert(2, 25)
    print("After insertions:", nums)

    popped = nums.pop()
    print(f"Popped element: {popped} | Current list: {nums}")

    nums.remove(25)
    print("After removing 25:", nums)

    # In-place sort vs sorted copy
    nums.sort(reverse=True)
    print("Descending sort:", nums)

    # Sublist slicing with step
    print("Every second item:", nums[::2])

if __name__ == "__main__":
    demonstrate_list_methods()
