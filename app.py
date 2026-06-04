import streamlit as st
from supabase import create_client

# Supabase Connection
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None


# Login Function
def login(username, password, role):

    result = (
        supabase.table("login_master")
        .select("*")
        .eq("username", username)
        .eq("password", password)
        .eq("role", role.lower())
        .execute()
    )

    return result.data


# Logout Function
def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.rerun()


# LOGIN PAGE
if not st.session_state.logged_in:

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.title("🎓 Student Management System")

        role = st.radio(
            "Login Type",
            ["Student", "Admin"],
            horizontal=True
        )

        username = st.text_input(
            "Username / Enrollment Number"
        )

        password = st.text_input(
            "Password / DOB",
            type="password"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            data = login(
                username,
                password,
                role
            )

            if data:

                st.session_state.logged_in = True
                st.session_state.user = data[0]

                st.rerun()

            else:
                st.error("Invalid Login Credentials")

# DASHBOARD
else:

    user = st.session_state.user

    st.sidebar.title("Menu")

    if st.sidebar.button("Logout"):
        logout()

    # ADMIN PANEL
    if user["role"] == "admin":

        st.title("🛠️ Admin Dashboard")

        menu = st.sidebar.selectbox(
            "Select",
            [
                "Dashboard",
                "Students"
            ]
        )

        if menu == "Dashboard":

            try:
                students = (
                    supabase.table("students")
                    .select("*")
                    .execute()
                )

                total_students = len(students.data)

            except:
                total_students = 0

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Total Students",
                total_students
            )

            c2.metric(
                "Admins",
                1
            )

            c3.metric(
                "Status",
                "Active"
            )

        elif menu == "Students":

            st.subheader("Students")

            try:

                students = (
                    supabase.table("students")
                    .select("*")
                    .execute()
                )

                st.dataframe(
                    students.data,
                    use_container_width=True
                )

            except Exception as e:

                st.error(str(e))

    # STUDENT PANEL
    else:

        st.title("🎓 Student Dashboard")

        menu = st.sidebar.selectbox(
            "Select",
            [
                "Profile"
            ]
        )

        if menu == "Profile":

            st.subheader("My Profile")

            st.write(
                "### Name:",
                user.get("student_name", "")
            )

            st.write(
                "### Enrollment No:",
                user.get("enrollment_no", "")
            )

            st.write(
                "### Username:",
                user.get("username", "")
            )

            st.json(user)
