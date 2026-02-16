
import streamlit as st
from utils.api import get_all_users, disable_user, enable_user, delete_user

st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)



# Protect page
if "access_token" not in st.session_state or not st.session_state.access_token:
    st.switch_page("pages/login.py")

if st.session_state.role != "ADMIN":
    st.warning("You do not have permission to access this page.")
    
    import time
    time.sleep(2)
    
    st.switch_page("pages/dashboard.py")


st.title("Manage Users")

users = get_all_users(st.session_state.access_token)

if "error" in users:
    st.error("Failed to load users")
    st.stop()

for user in users:
    st.markdown("---")
    st.write(f"ID: {user['id']}")
    st.write(f"Username: {user['username']}")
    st.write(f"Email: {user['email']}")
    st.write(f"Role: {user['role']}")
    st.write(f"Active: {user['is_active']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Disable", key=f"disable_{user['id']}"):
            disable_user(st.session_state.access_token, user["id"])
            st.rerun()

    with col2:
        if st.button("Enable", key=f"enable_{user['id']}"):
            enable_user(st.session_state.access_token, user["id"])
            st.rerun()

    with col3:
        if st.button("Delete", key=f"delete_{user['id']}"):
            delete_user(st.session_state.access_token, user["id"])
            st.rerun()

st.markdown("---")

if st.button("Back to Dashboard"):
    st.switch_page("pages/dashboard.py")
