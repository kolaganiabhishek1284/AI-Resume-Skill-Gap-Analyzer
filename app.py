import streamlit as st

st.title("AI Resume Skill Gap Analyzer")

resume_text = st.text_area("Paste your resume text here")

if st.button("Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please paste resume text.")
    else:
        st.subheader("AI Feedback")

        st.write("""
**Missing Technical Skills:**
- Advanced Python libraries
- Machine Learning algorithms
- SQL for data analysis

**Missing Soft Skills:**
- Communication
- Problem solving

**Improvements:**
- Add project impact with numbers
- Mention tools like Pandas, NumPy
- Include internships or certifications

**Resume Score:** 6.5 / 10

**ATS Tip:**
Use role-specific keywords like *Data Analysis*, *Machine Learning*, and *Python*.
""")
