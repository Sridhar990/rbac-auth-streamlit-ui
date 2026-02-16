import streamlit as st
from utils.api import forgot_password
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

st.title("Forgot Password")

email = st.text_input("Enter your registered email")

if st.button("Send OTP"):

    if not email:
        st.warning("Please enter your email")
    else:
        result = forgot_password(email)

        if "error" in result:
            error_detail = result["error"]
            if isinstance(error_detail, dict) and "detail" in error_detail:
                st.error(error_detail["detail"])
            else:
                st.error("Failed to send OTP")
        else:
            st.success("OTP sent to your email")

            st.session_state.reset_email = email

            import time
            time.sleep(2)

            st.switch_page("pages/reset_password.py")

st.markdown("---")

if st.button("Back to Login"):
    st.switch_page("pages/login.py")
