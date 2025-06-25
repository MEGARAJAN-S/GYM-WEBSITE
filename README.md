# 🏋️‍♂️ Gym Management System

A full-stack **Gym Website** built using **Django**. It helps manage gym operations like member registrations, plans, trainers, session bookings, and admin control — all with a clean and responsive UI.

---

## 📌 Features

- ✅ User Sign Up / Login / Logout
- ✅ Admin Dashboard
- ✅ Member Profile and Plan Management
- ✅ Trainer Listings
- ✅ Session Booking System
- ✅ Responsive Frontend (Bootstrap)
- ✅ Contact & Feedback Page

---

## 🛠️ Tech Stack

- **Backend**: Django, Python 3
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (easily swappable with PostgreSQL/MySQL)
- **Tools**: Django Admin, Django Forms, Crispy Forms

---

## 📂 Folder Structure

```bash
gym-website/
├── gymapp/ # Django app logic
│ ├── models.py # Models (User, Plan, Trainer, etc.)
│ ├── views.py # View functions
│ ├── forms.py # Django forms
│ └── urls.py # App routing
├── templates/ # HTML files
├── static/ # Static files (CSS/JS/images)
├── gymproject/ # Django project settings
│ ├── settings.py
│ └── urls.py
├── db.sqlite3 # Default database
├── manage.py
└── requirements.txt
```

---

## 🚀 Setup Instructions

### 🔧 Step-by-Step Commands

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/gym-website.git
cd gym-website
```
#### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
#### 4️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
#### 5️⃣ Create Superuser (Admin Access)
```bash
python manage.py runserver
```
Visit:
📍 http://127.0.0.1:8000/ for the site
🔐 http://127.0.0.1:8000/admin/ for the admin panel
Git Token : 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

🙋‍♂️ Author
Megarajan S.
🎓 B.Tech CSE | Shiv Nadar University, Chennai
