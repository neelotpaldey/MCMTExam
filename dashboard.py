import streamlit as st

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    role = st.radio(
        "Login Type",
        ["Student Login", "Admin Login"],
        horizontal=True
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        # Database Validation Here

        if role == "Admin Login":

            if username == "admin" and password == "admin123":

                st.session_state.logged_in = True
                st.session_state.role = "admin"
                st.rerun()

        else:

            if username == "student" and password == "123":

                st.session_state.logged_in = True
                st.session_state.role = "student"
                st.rerun()

else:

    if st.session_state.role == "admin":

        st.title("Admin Dashboard")

    else:

        st.title("Student Dashboard")
