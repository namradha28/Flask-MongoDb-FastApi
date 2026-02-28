FastAPI + MongoDB + Flask (Full Stack Application)

A modern full-stack web application built using FastAPI (Backend API), MongoDB (Database), and Flask (Frontend UI).

This project demonstrates REST API development, NoSQL database integration, and professional frontend-backend communication with a clean, responsive dashboard UI.

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

✅ View Students (GET API)

✅ Delete Student (DELETE API)

✅ MongoDB Integration

✅ Swagger API Documentation

✅ Responsive Dashboard UI

✅ Glassmorphism Design

✅ Clean Full Stack Architecture

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

MongoDB runs on:
mongodb://localhost:27017/

3️⃣ Setup Backend (FastAPI)

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend URL:
http://127.0.0.1:8000

Swagger Documentation:
http://127.0.0.1:8000/docs

4️⃣ Setup Frontend (Flask)

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
"email": "namradha@gmail.com
",
"course": "Data Engineering"
}

➤ Get All Students

GET /students/

➤ Delete Student

DELETE /students/{student_id}

💼 Resume Description

Developed a full-stack Student Management System using FastAPI, MongoDB, and Flask. Designed RESTful APIs with CRUD operations, integrated a NoSQL database, and built a modern responsive dashboard UI. Demonstrated backend API development, database handling, and seamless frontend integration in a production-style architecture.

🔥 Future Enhancements

JWT Authentication

Update (PUT) API

Search & Filtering

Pagination

Dockerization

AWS / Render Deployment

Role-Based Access Control

Admin Dashboard

Analytics Section

🧠 Learning Outcomes

REST API Design

NoSQL Database Integration

Full Stack Development

API Testing with Swagger

Frontend-Backend Integration

Clean Project Structuring

📄 License

This project is open-source and available for educational and portfolio purposes.

⭐ If you found this project helpful, consider giving it a star!
