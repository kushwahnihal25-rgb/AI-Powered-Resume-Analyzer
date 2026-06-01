import streamlit as st
import plotly.express as px

from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_calculator import calculate_score
from utils.ai_suggestions import get_suggestions

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.title("📄 AI Resume Analyzer")
st.caption("🚀 ATS Score • Skill Gap Analysis • AI Feedback")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if resume and jd:

    # Extract text and skills
    text = extract_text(resume)

    resume_skills = extract_skills(text)
    jd_skills = extract_skills(jd)

    # ATS Score
    score = calculate_score(
        resume_skills,
        jd_skills
    )

    st.metric(
        "ATS Score",
        f"{score}%"
    )

    st.progress(int(score))

    # Skills comparison
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Resume Skills")

        for skill in resume_skills:
            st.success(skill)

    with col2:
        st.subheader("🎯 JD Skills")

        for skill in jd_skills:
            st.info(skill)

    # Missing skills
    missing = list(
        set(jd_skills) - set(resume_skills)
    )

    st.subheader("❌ Missing Skills")

    if missing:
        for skill in missing:
            st.error(skill)
    else:
        st.success("No missing skills found 🎉")

    # Pie chart
    matched = len(
        set(resume_skills) & set(jd_skills)
    )

    missing_count = len(missing)

    fig = px.pie(
        values=[matched, missing_count],
        names=["Matched", "Missing"],
        title="📊 Skill Matching Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # AI Feedback
    st.subheader("🤖 AI Resume Feedback")

    if st.button("🤖 Generate AI Feedback"):

        feedback = get_suggestions(
            text,
            jd
        )

        with st.expander(
            "📄 View Detailed AI Analysis",
            expanded=True
        ):
            st.markdown(feedback)

        st.download_button(
            "📥 Download AI Report",
            feedback,
            file_name="resume_analysis.txt"
        )