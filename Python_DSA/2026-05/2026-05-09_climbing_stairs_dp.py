"""DP Intro: Climbing Stairs and Min Cost Climbing Stairs."""

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

def min_cost_climbing_stairs(cost: list[int]) -> int:
    prev2, prev1 = cost[0], cost[1]
    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr
    return min(prev1, prev2)

if __name__ == "__main__":
    print("Climbing 5 stairs ways:", climb_stairs(5))
    costs = [10, 15, 20]
    print("Min cost climbing stairs:", min_cost_climbing_stairs(costs))
