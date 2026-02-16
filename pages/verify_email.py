import streamlit as st
from utils.api import verify_email
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

st.title("Verify Email")

# If no registered email, redirect to register
if "registered_email" not in st.session_state:
    st.switch_page("pages/register.py")

email = st.session_state.registered_email

st.write(f"Email: {email}")

otp = st.text_input("Enter OTP")

if st.button("Verify"):

    if not otp:
        st.warning("Please enter OTP")
    else:
        result = verify_email(email, otp)

        if "error" in result:
            error_detail = result["error"]
            if isinstance(error_detail, dict) and "detail" in error_detail:
                st.error(error_detail["detail"])
            else:
                st.error("Verification failed")
        else:
            st.success("Registration completed successfully! You can now login.")

            
            # Clear session email
            del st.session_state.registered_email

            import time
            time.sleep(2)

            
            st.switch_page("pages/login.py")

st.markdown("---")

if st.button("Back to Login"):
    st.switch_page("pages/login.py")

