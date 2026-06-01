import os
import streamlit as st
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except:
        api_key = None

print("API Key Found:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def get_suggestions(resume_text, job_description):
    prompt = f"""
    Analyze this resume and compare it with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:
    1. Missing skills
    2. Resume improvements
    3. ATS optimization tips
    4. Project suggestions

    Keep response short.
    """

    response = model.generate_content(prompt)
    return response.text
print("API Key Found:", api_key is not None)
print("Key Length:", len(api_key) if api_key else 0)