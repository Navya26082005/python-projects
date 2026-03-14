# Sample skills list
skills_list = ["python", "java", "machine learning", "sql", "nlp", "data analysis"]

def analyze_resume(resume_text):
    resume_text = resume_text.lower()
    found_skills = [skill for skill in skills_list if skill in resume_text]
    print("Skills found:", found_skills)

# Example usage
resume_text = """
Navya Salomi has knowledge in Python, Machine Learning, and Data Analysis.
"""
analyze_resume(resume_text)