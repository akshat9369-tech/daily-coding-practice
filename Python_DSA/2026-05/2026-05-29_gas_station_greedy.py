"""Greedy: Gas Station Circular Tour Problem."""

def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    total_tank, curr_tank = 0, 0
    start_station = 0

    for i in range(len(gas)):
        net = gas[i] - cost[i]
        total_tank += net
        curr_tank += net

        if curr_tank < 0:
            start_station = i + 1
            curr_tank = 0

    return start_station

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print("Starting gas station index:", can_complete_circuit(gas, cost))
