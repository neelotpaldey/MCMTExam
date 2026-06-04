if st.session_state.role == "admin":

    st.title("Admin Dashboard")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Students",120)
    c2.metric("Courses",8)
    c3.metric("Attendance",85)
    c4.metric("Results",92)

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Students",
            "Attendance",
            "Results",
            "Settings"
        ]
    )

else:

    st.title("Student Dashboard")

    c1,c2,c3 = st.columns(3)

    c1.metric("Attendance","88%")
    c2.metric("Marks","76")
    c3.metric("Assignments","4")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Profile",
            "Attendance",
            "Marks",
            "Assignments"
        ]
    )
