import streamlit as st
from supabase import create_client

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login(username, password):
    result = supabase.table("login_master").select("*").eq("username", username).eq("password", password).execute()
    return result.data

if not st.session_state.logged_in:
    st.title("Student/Admin Login")

    role = st.radio("Login Type", ["Student", "Admin"], horizontal=True)

    username = st.text_input("Username / Enrollment No")
    password = st.text_input("Password / DOB", type="password")

    if st.button("Login"):
        data = login(username, password)
        if data:
            st.session_state.logged_in = True
            st.session_state.user = data[0]
            st.rerun()
        else:
            st.error("Invalid Credentials")

else:
    user = st.session_state.user

    if user["role"] == "admin":
        st.title("Admin Dashboard")

        menu = st.sidebar.selectbox(
            "Menu",
            ["Home", "Students"]
        )

        if menu == "Home":
            st.success("Welcome Admin")

        if menu == "Students":
            st.subheader("All Students")

            students = supabase.table("students").select("*").execute()
            st.dataframe(students.data)

    else:
        st.title("Student Dashboard")

        menu = st.sidebar.selectbox(
            "Menu",
            ["Profile"]
        )

        if menu == "Profile":
            st.write(user)

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()
