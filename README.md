🎓 Student Management System
FastAPI + MongoDB + Flask (Full Stack Project)

A modern full-stack web application built using FastAPI (Backend API), MongoDB (Database), and Flask (Frontend UI).

This project demonstrates REST API development, NoSQL database integration, frontend-backend communication, and a professional dashboard UI suitable for portfolio and resume use.

🚀 Tech Stack
🔹 Backend

FastAPI

Uvicorn

PyMongo

Pydantic

🔹 Database

MongoDB (NoSQL)

🔹 Frontend

Flask

HTML5

CSS3 (Modern Dashboard UI)

Jinja2 Templates

✨ Features

✅ Create Student (POST API)

✅ View All Students (GET API)

✅ Delete Student (DELETE API)

✅ MongoDB Integration

✅ Swagger API Documentation

✅ Clean Modern Dashboard UI

✅ Responsive Design

✅ Glassmorphism Styling

🏗 Architecture

Flask Frontend
↓
FastAPI REST API
↓
MongoDB Database

📂 Project Structure

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

⚙️ Installation & Setup
1️⃣ Clone Repository

git clone https://github.com/your-username/fastapi-flask-mongo.git

cd fastapi-flask-mongo

2️⃣ Setup MongoDB

Make sure MongoDB is installed and running:

mongod

MongoDB default URL:
mongodb://localhost:27017/

3️⃣ Setup Backend (FastAPI)

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs on:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

4️⃣ Setup Frontend (Flask)

Open a new terminal:

cd frontend
pip install flask requests
python app.py

Frontend runs on:
http://127.0.0.1:5000

📬 API Endpoints
➤ Create Student

POST /students/

Example JSON:

{
"name": "Namradha",
"email": "namradha@gmail.com
",
"course": "Data Engineering"
}

➤ Get All Students

GET /students/

➤ Delete Student

DELETE /students/{student_id}
