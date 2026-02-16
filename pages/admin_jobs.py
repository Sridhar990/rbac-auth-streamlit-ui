
import streamlit as st
from utils.api import create_job, delete_job, get_jobs

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


st.title("Admin - Manage Jobs")

# Create Job 
st.subheader("Create New Job")

company_name = st.text_input("Company Name")
role = st.text_input("Role")
application_end_date = st.date_input("Application End Date")
job_link = st.text_input("Job Link")

if st.button("Create Job"):

    if not company_name or not role or not job_link:
        st.warning("All fields are required")
    else:
        result = create_job(
            st.session_state.access_token,
            company_name,
            role,
            str(application_end_date),
            job_link
        )

        if "error" in result:
            st.error("Failed to create job")
        else:
            st.success("Job created successfully!")
            st.rerun()

st.markdown("---")

# Existing Jobs 
st.subheader("Existing Jobs")

jobs = get_jobs(st.session_state.access_token)

if "error" in jobs:
    st.error("Failed to load jobs")
else:
    if not jobs:
        st.info("No jobs available")
    else:
        for job in jobs:
            st.markdown(f"### {job['company_name']} - {job['role']}")
            st.write(f"Apply before: {job['application_end_date']}")
            st.write(f"Link: {job['job_link']}")

            if st.button("Delete", key=f"delete_{job['id']}"):
                delete_job(st.session_state.access_token, job["id"])
                st.success("Job deleted")
                st.rerun()

            st.markdown("---")

if st.button("Back to Dashboard"):
    st.switch_page("pages/dashboard.py")

