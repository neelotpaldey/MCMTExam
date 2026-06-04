import streamlit as st
from supabase import create_client

supabase = create_client(
    st.secrets["https://gnvhtcjxfhslmfcxjrkw.supabase.co"],
    st.secrets["sb_publishable_I0wxHRThBD0BORVHmtcjEw_FvvkiYYz"]
)

st.title("Supabase Connection Test")

result = supabase.table("login_master").select("*").execute()

st.write(result.data)
