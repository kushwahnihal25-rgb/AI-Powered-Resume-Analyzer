import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except:
        api_key = None

print("API Key Found:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

def get_suggestions(resume_text, job_description):

    prompt = f"""
    Compare resume and job description.

    Resume:
    {resume_text[:3000]}

    Job Description:
    {job_description[:1500]}

    Give:
    1. Missing skills
    2. Improvements
    3. ATS tips
    4. Project ideas

    Short answer.
    """

    response = model.generate_content(prompt)
    return response.text

    response = model.generate_content(prompt)
    return response.text
print("API Key Found:", api_key is not None)
print("Key Length:", len(api_key) if api_key else 0)
import os

print("Current Folder:", os.getcwd())
print("ENV KEY:", os.getenv("GEMINI_API_KEY"))