import streamlit as st
from utils.api import login_user, get_current_user

st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)


st.title("Login")

# If already logged in → go to dashboard
if "access_token" in st.session_state and st.session_state.access_token:
    st.switch_page("pages/dashboard.py")

username = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if not username or not password:
        st.warning("Please enter email and password")

    else:
        result = login_user(username, password)

        if "error" in result:
            st.error("Invalid credentials")

        else:
            # Store access token
            st.session_state.access_token = result["access_token"]

            # Fetch user details to get role
            user = get_current_user(st.session_state.access_token)

            if "error" in user:
                st.error("Failed to fetch user details")
            else:
                st.session_state.role = user["role"]
                st.success("Login successful!")
                st.switch_page("pages/dashboard.py")

st.markdown("---")
st.markdown("Don't have an account?")

col1, col2 = st.columns(2)

with col1:
    if st.button("Go to Register"):
        st.switch_page("pages/register.py")

with col2:
    if st.button("Forgot Password"):
        st.switch_page("pages/forgot_password.py")



