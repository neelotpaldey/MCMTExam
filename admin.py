import streamlit as st
from database import supabase

def admin_dashboard():

    st.title("Admin Dashboard")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Dashboard",
            "Add Student",
            "View Students"
        ]
    )

    if menu == "Dashboard":

        total_students = supabase.table("students").select("*").execute()

        st.metric(
            "Total Students",
            len(total_students.data)
        )

    elif menu == "Add Student":

        st.subheader("Add Student")

        enrollment = st.text_input("Enrollment No")
        name = st.text_input("Student Name")
        father = st.text_input("Father Name")
        mobile = st.text_input("Mobile")
        course = st.text_input("Course")
        semester = st.text_input("Semester")

        if st.button("Save Student"):

            supabase.table("students").insert({
                "enrollment_no": enrollment,
                "student_name": name,
                "father_name": father,
                "mobile": mobile,
                "course": course,
                "semester": semester
            }).execute()

            st.success("Student Added Successfully")

    elif menu == "View Students":

        students = supabase.table(
            "students"
        ).select("*").execute()

        st.dataframe(students.data)
