"""Sliding Window: Fruit Into Baskets (At Most 2 Types)."""

def total_fruit(fruits: list[int]) -> int:
    basket = {}
    left = 0
    max_fruits = 0

    for right, fruit in enumerate(fruits):
        basket[fruit] = basket.get(fruit, 0) + 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

if __name__ == "__main__":
    trees = [1, 2, 3, 2, 2]
    print("Max fruit picked:", total_fruit(trees))
