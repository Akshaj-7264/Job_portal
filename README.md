# 🧑‍💼 Job Portal - Django Web App

A modern and professional job portal built with Django, supporting two user roles: **Job Seekers** and **Recruiters**. Users can register, post jobs, apply to jobs, and manage applications in an intuitive dashboard with dynamic UI and clean design.

---

## 🚀 Features

### 🔐 Authentication
- User Registration & Login (with email confirmation support)
- Password Reset & Change functionality
- Separate dashboards for **Recruiters** and **Job Seekers**

### 🧑‍💼 Job Seekers
- Browse job listings (local + Adzuna API)
- Apply for local jobs with a detailed form
- View and manage submitted applications

### 🧑‍💼 Recruiters
- Post new jobs
- View applicants for each job
- Approve or reject applications (with email notifications)

### 🎨 UI
- Professional modern styling
- Navbar dynamically shown/hidden based on route
- Password toggle (eye icon) on login/register forms

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default) – easily switchable to PostgreSQL
- **Email Backend**: Console (for dev), customizable for SMTP
- **3rd Party**: [Adzuna Job Search API](https://developer.adzuna.com/)

---

## 📂 Project Structure

```
job_portal/
├── accounts/               # Handles user auth, registration, login
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── jobs/                   # Core job functionalities
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── accounts/
│   ├── jobs/
│   └── dashboard/
│
├── static/                 # Static files (CSS, JS, images)
│   ├── style/
│   └── js/
│
├── media/                  # Uploaded resumes
│
├── manage.py
├── requirements.txt
└── job_portal/             # Project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## ⚙️ Setup Instructions

### 1. 🔽 Clone the repository

```bash
git clone https://github.com/yourusername/job_portal.git
cd job_portal
```

### 2. 🧪 Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 4. 🗂️ Apply migrations

```bash
python manage.py migrate
```

### 5. 👤 Create superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. ▶️ Run development server

```bash
python manage.py runserver
```

Then visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📧 Configure Email (Optional)

For real email sending:

In `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

---

## 🚀 Deployment

- Compatible with **Render**, **Railway**, **Vercel (with API)**, and **Heroku**
- Set up a `start.sh` and `render.yaml` or `Procfile` depending on platform
- Make sure to run:
  ```bash
  python manage.py migrate
  ```

---

## 📝 License

MIT License. Free to use and modify.