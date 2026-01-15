"""Sets: Set Operations, Hash Sets, and Uniqueness."""

def set_algebra():
    frontend_skills = {"HTML", "CSS", "JavaScript", "TypeScript", "React"}
    backend_skills = {"Python", "Django", "PostgreSQL", "Docker", "TypeScript"}

    print("Frontend skills:", frontend_skills)
    print("Backend skills :", backend_skills)

    # Set operations
    shared = frontend_skills & backend_skills
    all_skills = frontend_skills | backend_skills
    front_only = frontend_skills - backend_skills
    unique_either = frontend_skills ^ backend_skills

    print(f"Intersection (Shared)        : {shared}")
    print(f"Union (All skills)           : {all_skills}")
    print(f"Difference (Frontend only)   : {front_only}")
    print(f"Symmetric Difference         : {unique_either}")

if __name__ == "__main__":
    set_algebra()
