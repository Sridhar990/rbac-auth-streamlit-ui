import streamlit as st
from utils.api import register_user
import time

st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)


if "access_token" in st.session_state and st.session_state.access_token:
    st.warning("You are already logged in.")

    time.sleep(1)

    st.switch_page("pages/dashboard.py")

st.title("Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):

    if not username or not email or not password:
        st.warning("All fields are required")

    elif password != confirm_password:
        st.warning("Passwords do not match")

    else:
        result = register_user(username, email, password)

        if "error" in result:
            error_detail = result["error"]
            if isinstance(error_detail, dict) and "detail" in error_detail:
                st.error(error_detail["detail"])
            else:
                st.error("Registration failed")

        else:
            st.success("OTP sent successfully to your email!")
            st.session_state.registered_email = email

            st.info("Redirecting to OTP verification page...")

            import time
            time.sleep(2)

            st.switch_page("pages/verify_email.py")


st.markdown("---")

if st.button("Back to Login"):
    st.switch_page("pages/login.py")

