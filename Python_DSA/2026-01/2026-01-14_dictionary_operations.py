"""Dictionaries: Hash Map Fundamentals and Dict Comprehensions."""

def dictionary_features():
    student_scores = {
        "Akshat": 95,
        "David": 78,
        "Elena": 88,
        "Grace": 92
    }

    # Safe lookup with get
    print("Lookup 'David':", student_scores.get("David"))
    print("Lookup 'Zack' (default):", student_scores.get("Zack", 0))

    # Updating and iterating
    student_scores["Zack"] = 84
    print("\nStudent Directory:")
    for name, score in sorted(student_scores.items(), key=lambda item: item[1], reverse=True):
        print(f"  {name:8s} : {score} pts")

    # Dict comprehension for scaling scores
    curved_scores = {name: min(100, score + 5) for name, score in student_scores.items()}
    print("\nCurved Scores (+5):", curved_scores)

if __name__ == "__main__":
    dictionary_features()
