import streamlit as st


st.set_page_config(page_title="RBAC System", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)



# Initialize session state safely
if "access_token" not in st.session_state:
    st.session_state.access_token = None

if "role" not in st.session_state:
    st.session_state.role = None

# If already logged in redirect to dashboard
if st.session_state.access_token:
    st.switch_page("pages/dashboard.py")

st.title("RBAC Authentication System with Job Portal")

st.markdown("""
## What This System Provides

This is a Role-Based Access Control (RBAC) system built with:

- FastAPI Backend
- JWT Authentication
- OTP Email Verification
- MySQL Database
- Streamlit Frontend

### Features

- Secure user registration with OTP verification
- JWT-based login authentication
- Role-based access (Admin / User)
- Admin job posting system
- User job viewing system
- Profile management
- Password change and reset via OTP

This system demonstrates a complete backend authentication architecture integrated with a frontend.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("Login"):
        st.switch_page("pages/login.py")

with col2:
    if st.button("Register"):
        st.switch_page("pages/register.py")
