# 🎓 Student Management System  
## 🚀 FastAPI + MongoDB + Flask (Full Stack Production-Style Project)

A modern, full-stack web application built using **FastAPI (Backend API)**, **MongoDB (NoSQL Database)**, and **Flask (Frontend UI)**.

This project demonstrates REST API development, NoSQL database integration, clean architecture, and professional frontend-backend communication. Designed as a resume-ready, portfolio-grade application.

---

# 🌐 Live Architecture Overview

Flask Frontend  
⬇  
FastAPI REST API  
⬇  
MongoDB Database  

---

# 🛠 Tech Stack

## 🔹 Backend
- FastAPI
- Uvicorn (ASGI Server)
- PyMongo
- Pydantic
- Python 3.x

## 🔹 Database
- MongoDB (NoSQL, Document-based)

## 🔹 Frontend
- Flask
- HTML5
- CSS3 (Modern Dashboard UI)
- Jinja2 Templates

---

# ✨ Core Features

- ✅ Create Student (POST API)
- ✅ View Students (GET API)
- ✅ Delete Student (DELETE API)
- ✅ MongoDB Document Storage
- ✅ RESTful API Architecture
- ✅ Swagger Documentation (/docs)
- ✅ Modern Glassmorphism Dashboard
- ✅ Responsive UI Design
- ✅ Clean Folder Structure
- ✅ Full Stack Integration

---

# 📂 Project Structure
fastapi-flask-mongo/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ └── requirements.txt
│
├── frontend/
│ ├── app.py
│ ├── templates/
│ │ ├── index.html
│ │ └── add.html
│ └── static/
│ └── style.css
│
└── README.md


---

# ⚙️ Installation & Setup Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-flask-mongo.git
cd fastapi-flask-mongo

Install MongoDB
Make sure MongoDB is installed and running:
mongod

Setup Backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend URL:
http://127.0.0.1:8000

Swagger Documentation:
http://127.0.0.1:8000/docs

Setup Frontend (Flask)
Open a new terminal:

cd frontend
pip install flask requests
python app.py

Frontend URL:
http://127.0.0.1:5000

📬 API Endpoints
➤ Create Student

POST /students/

Example JSON:

{
  "name": "Namradha",
  "email": "namradha@gmail.com",
  "course": "Data Engineering"
}
➤ Get All Students

GET /students/
Returns list of student documents stored in MongoDB.

➤ Delete Student
DELETE /students/{student_id}
Removes student document using MongoDB ObjectId.

🖥 UI Highlights
Modern gradient background
Glassmorphism styled cards
Responsive data table
Styled action buttons
Clean form layout
Professional dashboard feel

🧠 Concepts Demonstrated
REST API Design
NoSQL Document Modeling
FastAPI Dependency Injection
Backend-Frontend Communication
HTTP Methods (GET, POST, DELETE)
JSON Serialization
Modular Project Structure
Production-style UI Design
