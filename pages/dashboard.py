import streamlit as st
from utils.api import get_jobs

st.set_page_config(page_title="Dashboard", layout="wide")

# Hide  sidebar pages
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

st.sidebar.title("Navigation")

# Role-based menu
if st.session_state.role == "ADMIN":
    menu = st.sidebar.radio(
        "Go to",
        ["Home", "Manage Users", "Manage Jobs", "Profile", "Change Password"]
    )
else:
    menu = st.sidebar.radio(
        "Go to",
        ["Home", "Profile", "Change Password"]
    )

if st.sidebar.button("Logout"):
    st.session_state.access_token = None
    st.session_state.role = None
    st.switch_page("app.py")

# HOME 
if menu == "Home":
    st.title("Dashboard")
    st.markdown(f"### Logged in as: {st.session_state.role}")
    st.markdown("---")

    jobs = get_jobs(st.session_state.access_token)

    if "error" in jobs:
        st.error("Failed to load jobs")
    else:
        if not jobs:
            st.info("No jobs available.")
        else:
            st.subheader("Available Jobs")

            for job in jobs:
                with st.container():
                    st.markdown(f"### {job['company_name']} - {job['role']}")
                    st.write(f"Apply before: {job['application_end_date']}")
                    st.markdown(f"[Apply Here]({job['job_link']})")
                    st.markdown("--")
elif menu == "Manage Users":
    st.switch_page("pages/admin_users.py")


elif menu == "Manage Jobs":
    st.switch_page("pages/admin_jobs.py")


elif menu == "Profile":
    st.switch_page("pages/profile.py")


elif menu == "Change Password":
    st.switch_page("pages/password_change.py")
