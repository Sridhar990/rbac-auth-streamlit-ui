import streamlit as st
from utils.api import get_current_user, update_profile

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

st.title("My Profile")

user = get_current_user(st.session_state.access_token)

if "error" in user:
    st.error("Failed to load profile")
    st.stop()

# Display basic info
st.subheader("Account Info")
st.write(f"Username: {user['username']}")
st.write(f"Email: {user['email']}")
st.write(f"Role: {user['role']}")

st.markdown("---")

# Profile form
st.subheader("Update Profile")

profile = user.get("profile", {})

full_name = st.text_input("Full Name", profile.get("full_name", ""))
phone_number = st.text_input("Phone Number", profile.get("phone_number", ""))
address = st.text_input("Address", profile.get("address", ""))

if st.button("Update Profile"):

    data = {
        "full_name": full_name,
        "phone_number": phone_number,
        "address": address
    }

    result = update_profile(st.session_state.access_token, data)

    if "error" in result:
        st.error("Failed to update profile")
    else:
        st.success("Profile updated successfully!")

if st.button("Back to Dashboard"):
    st.switch_page("pages/dashboard.py")
