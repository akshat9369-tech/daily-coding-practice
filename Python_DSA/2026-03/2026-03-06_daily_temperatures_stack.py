"""Stack: Daily Temperatures Monotonic Stack Problem."""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices of unresolved temperatures

    for curr_day, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = curr_day - prev_day
        stack.append(curr_day)

    return answer

if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print("Temps :", temps)
    print("Wait  :", daily_temperatures(temps))
