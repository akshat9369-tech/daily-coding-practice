"""Conditional Branching and Match-Case Statements."""

def classify_grade(score: float) -> str:
    if not (0 <= score <= 100):
        return "Invalid Score"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def describe_http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unhandled Status ({status_code})"

if __name__ == "__main__":
    scores = [95, 82, 74, 55, 105]
    for s in scores:
        print(f"Score {s:3d} -> Grade {classify_grade(s)}")

    for code in [200, 404, 500, 418]:
        print(f"HTTP {code} -> {describe_http_status(code)}")
