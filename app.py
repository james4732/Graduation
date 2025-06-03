
import streamlit as st
import pandas as pd

# Load student data
@st.cache_data
def load_data():
    return pd.read_csv("sample_student_list.csv")

df = load_data()

st.set_page_config(page_title="Graduation Display", layout="wide")

# Simulate scanned ID input (from QR code)
student_id = st.text_input("Scan QR Code / Enter Student ID", max_chars=10)

# Layout: Two-column - Display & Announcer View
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎓 Main Display")
    if student_id:
        student = df[df["Student_ID"] == student_id.upper()]
        if not student.empty:
            row = student.iloc[0]
            st.image(row["Photo_URL"], width=200)
            st.subheader(row["Full_Name"])
            st.write(f"🏅 {row['Award_Title']}")
        else:
            st.warning("Student ID not found.")
    else:
        st.info("Awaiting scan...")

with col2:
    st.header("🎤 Announcer View")
    if student_id and not student.empty:
        st.markdown(f"## {row['Full_Name']}")
        st.markdown(f"**Award:** {row['Award_Title']}")
    elif not student_id:
        st.markdown("Please scan a student's QR code.")
