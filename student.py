import streamlit as st
from database import supabase

def student_dashboard(user):

    st.title("Student Dashboard")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Profile",
            "Attendance",
            "Marks"
        ]
    )

    if menu == "Profile":

        st.subheader("Student Profile")

        st.write("Name :", user["student_name"])
        st.write("Enrollment :", user["enrollment_no"])

    elif menu == "Attendance":

        attendance = supabase.table(
            "attendance"
        ).select("*").eq(
            "enrollment_no",
            user["enrollment_no"]
        ).execute()

        st.dataframe(attendance.data)

    elif menu == "Marks":

        marks = supabase.table(
            "marks"
        ).select("*").eq(
            "enrollment_no",
            user["enrollment_no"]
        ).execute()

        st.dataframe(marks.data)
