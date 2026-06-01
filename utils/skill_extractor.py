skills_database = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "sql",
    "power bi",
    "excel",
    "tensorflow",
    "pandas",
    "numpy",
    "streamlit"
]

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in skills_database:
        if skill in text:
            found.append(skill)

    return found