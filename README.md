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

