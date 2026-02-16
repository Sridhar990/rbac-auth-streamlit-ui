import streamlit as st
from utils.api import reset_password
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

st.title("Reset Password")

# If no email stored → redirect
if "reset_email" not in st.session_state:
    st.switch_page("pages/forgot_password.py")

email = st.session_state.reset_email

st.write(f"Email: {email}")

otp = st.text_input("Enter OTP")
new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm New Password", type="password")

if st.button("Reset Password"):

    if not otp or not new_password:
        st.warning("All fields are required")

    elif new_password != confirm_password:
        st.warning("Passwords do not match")

    else:
        result = reset_password(email, otp, new_password)

        if "error" in result:
            error_detail = result["error"]
            if isinstance(error_detail, dict) and "detail" in error_detail:
                st.error(error_detail["detail"])
            else:
                st.error("Reset failed")
        else:
            st.success("Password reset successful! Please login.")

            # Clear stored email
            del st.session_state.reset_email

            import time
            time.sleep(2)

            st.switch_page("pages/login.py")

st.markdown("---")

if st.button("Back to Login"):
    st.switch_page("pages/login.py")

