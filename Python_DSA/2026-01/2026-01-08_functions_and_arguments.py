"""Functions, Default Arguments, and Variable Length (*args, **kwargs)."""

def compute_statistics(*values: float, precision: int = 2) -> dict:
    if not values:
        return {"count": 0, "mean": 0.0, "min": 0.0, "max": 0.0}

    total = sum(values)
    count = len(values)
    mean = round(total / count, precision)

    return {
        "count": count,
        "mean": mean,
        "min": min(values),
        "max": max(values)
    }

def build_profile(username: str, email: str, **attributes):
    profile = {"username": username, "email": email}
    profile.update(attributes)
    return profile

if __name__ == "__main__":
    stats = compute_statistics(12.5, 45.0, 78.2, 90.1, 33.4, precision=3)
    print("Computed Stats:", stats)

    user = build_profile("akshat_dev", "akshat@example.com", role="Engineer", location="Remote", active=True)
    print("User Profile:", user)
