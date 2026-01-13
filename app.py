from ai_logic.skill_to_project import generate_project

skills = ["Python", "SQL", "Data Analysis"]

projects = generate_project(skills)

print("Suggested Projects:")
for p in projects:
    print("-", p)
