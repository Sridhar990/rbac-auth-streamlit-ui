import requests
from config import BASE_URL


def login_user(email: str, password: str):
    url = f"{BASE_URL}/auth/login"

    data = {
        "username": email,
        "password": password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}


def get_current_user(token: str):
    url = f"{BASE_URL}/users/me"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}
    

# jobs 
def get_jobs(token: str):
    url = f"{BASE_URL}/jobs/"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}

# profile

def update_profile(token: str, data: dict):
    url = f"{BASE_URL}/users/update_profile"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.patch(url, json=data, headers=headers)

    try:
        response_data = response.json()
    except Exception:
        response_data = {"detail": response.text}

    if response.status_code in [200, 201]:
        return response_data
    else:
        return {"error": response_data}



#admin access 

def get_all_users(token: str):
    url = f"{BASE_URL}/admin/users"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}


def disable_user(token: str, user_id: int):
    url = f"{BASE_URL}/admin/users/{user_id}/disable"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.patch(url, headers=headers)

    return response.status_code


def enable_user(token: str, user_id: int):
    url = f"{BASE_URL}/admin/users/{user_id}/enable"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.patch(url, headers=headers)

    return response.status_code


def delete_user(token: str, user_id: int):
    url = f"{BASE_URL}/admin/users/{user_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(url, headers=headers)

    return response.status_code


#register AUth
def register_user(username: str, email: str, password: str):
    url = f"{BASE_URL}/auth/register"

    data = {
        "username": username,
        "email": email,
        "password": password
    }

    response = requests.post(url, json=data)

    if response.status_code in [200,201]:
        return response.json()
    else:
        return {"error": response.json()}


#verify email
def verify_email(email: str, otp: str):
    url = f"{BASE_URL}/auth/verify-email"

    data = {
        "email": email,
        "otp": otp
    }

    response = requests.post(url, json=data)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        return {"error": response.json()}



#forgot password

def forgot_password(email: str):
    url = f"{BASE_URL}/auth/forgot-password"

    data = {
        "email": email
    }

    response = requests.post(url, json=data)

    try:
        response_data = response.json()
    except:
        response_data = {"detail": response.text}

    if response.status_code in [200, 201]:
        return response_data
    else:
        return {"error": response_data}


# reset password
def reset_password(email: str, otp: str, new_password: str):
    url = f"{BASE_URL}/auth/reset-password"

    data = {
        "email": email,
        "otp": otp,
        "new_password": new_password
    }

    response = requests.post(url, json=data)

    try:
        response_data = response.json()
    except:
        response_data = {"detail": response.text}

    if response.status_code in [200, 201]:
        return response_data
    else:
        return {"error": response_data}


#change password

def change_password(token: str, old_password: str, new_password: str):
    url = f"{BASE_URL}/users/password_change"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "old_password": old_password,
        "new_password": new_password
    }

    response = requests.patch(url, json=data, headers=headers)

    try:
        response_data = response.json()
    except:
        response_data = {"detail": response.text}

    if response.status_code in [200, 201]:
        return response_data
    else:
        return {"error": response_data}
    

# create jobs
def create_job(token: str, company_name: str, role: str, application_end_date: str, job_link: str):
    url = f"{BASE_URL}/admin/jobs"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "company_name": company_name,
        "role": role,
        "application_end_date": application_end_date,
        "job_link": job_link
    }

    response = requests.post(url, json=data, headers=headers)

    try:
        response_data = response.json()
    except:
        response_data = {"detail": response.text}

    if response.status_code in [200, 201]:
        return response_data
    else:
        return {"error": response_data}

#delete

def delete_job(token: str, job_id: int):
    url = f"{BASE_URL}/admin/jobs/{job_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(url, headers=headers)

    return response.status_code
