from supabase import create_client
import streamlit as st

supabase = create_client(
    st.secrets["https://gnvhtcjxfhslmfcxjrkw.supabase.co"],
    st.secrets["sb_publishable_I0wxHRThBD0BORVHmtcjEw_FvvkiYYz"]
)
