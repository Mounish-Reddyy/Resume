import streamlit as st
from resume_parser import extract_text, parse_resume

st.set_page_config(page_title="Resume Parser", page_icon="📄", layout="centered")

st.title("📄 AI Resume Parser")
st.write("Upload your resume (PDF or DOCX), and I’ll extract key information automatically!")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("Extracting data..."):
        try:
            text = extract_text(uploaded_file)
            result = parse_resume(text)

            st.success("✅ Resume parsed successfully!")
            st.subheader("Extracted Information:")
            for key, value in result.items():
                st.write(f"**{key}:** {value}")
        except Exception as e:
            st.error(f"Error: {e}")
