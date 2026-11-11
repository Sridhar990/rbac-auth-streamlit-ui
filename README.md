![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![AWS](https://img.shields.io/badge/Deployment-AWS%20EC2-orange)


## 🔐RBAC Authentication System – Streamlit Frontend

### 📌Overview

This repository contains the Streamlit-based frontend UI for a Role-Based Access Control (RBAC) Authentication System.
The frontend communicates with a FastAPI backend API to handle:

* Authentication

* Authorization

* OTP email verification

* User and admin management

* This project demonstrates separation of frontend and backend architecture.



### 🚀Features

* User Registration

* Email Verification (OTP)

* Secure Login

* Role-Based Dashboard (Admin / User)

* Password Reset

* Password Change

* Profile Management

* Admin User Management

* Admin Job Management

### 🛠Tech Stack

* Python

* Streamlit

* Requests (for API communication)

 
### 📂Project Structure
```
rbac-auth-streamlit-ui/

├── app.py

├── config.py

├── requirements.txt

├── pages/

│   ├── login.py

│   ├── register.py

│   ├── dashboard.py

│   ├── admin_users.py

│   ├── admin_jobs.py

│   └── ...

├── utils/

│   └── api.py


└── .gitignore
```

  
### 🔗Backend API

This frontend connects to a FastAPI backend service.

Backend repository:
(You will add link after pushing backend project)


  

### ▶️Run Locally

#### 1️⃣.Clone the repository

 `git clone https://github.com/Sridhar990/rbac-auth-streamlit-ui.git`
 
  `cd rbac-auth-streamlit-ui`

 
#### 2️⃣.Install dependencies

  `pip install -r requirements.txt`

  
#### 3️⃣.Start backend server (must run on)

  `http://127.0.0.1:8000`

  
#### 4️⃣.Run Streamlit app

  `streamlit run app.py`


    
### ⚙️Configuration

The application reads backend API base URL from config.py.

> [!Note]
> Default: http://127.0.0.1:8000
> This can be overridden using environment variables for production deployment.


### 🏗Architecture

* Frontend: Streamlit
* Backend: FastAPI
* Database: MySQL
* Deployment: AWS EC2 + Nginx + Gunicorn

### 🔗 Related Repository

This Streamlit frontend communicates with the backend API:

Backend:https:[fastapi-rbac-auth-api](//github.com/Sridhar990/fastapi-rbac-auth-api)




