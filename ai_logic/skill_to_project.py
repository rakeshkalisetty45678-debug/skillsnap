def generate_project(skills):
    projects = {
        "python": "AI Resume Analyzer",
        "sql": "Sales Data Analysis Dashboard",
        "data analysis": "Business Insights Dashboard",
    }

    result = []
    for skill in skills:
        if skill.lower() in projects:
            result.append(projects[skill.lower()])

    return result
