import streamlit as st
from utils.api import change_password

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

st.title("Change Password")

old_password = st.text_input("Current Password", type="password")
new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm New Password", type="password")

if st.button("Change Password"):

    if not old_password or not new_password:
        st.warning("All fields are required")

    elif new_password != confirm_password:
        st.warning("New passwords do not match")

    else:
        result = change_password(
            st.session_state.access_token,
            old_password,
            new_password
        )

        if "error" in result:
            error_detail = result["error"]
            if isinstance(error_detail, dict) and "detail" in error_detail:
                st.error(error_detail["detail"])
            else:
                st.error("Password change failed")
        else:
            st.success("Password changed successfully!")

            import time
            time.sleep(2)

            st.switch_page("pages/dashboard.py")

st.markdown("---")

if st.button("Back to Dashboard"):
    st.switch_page("pages/dashboard.py")
