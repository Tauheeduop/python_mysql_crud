# 🧩 Python MySQL CRUD (FastAPI + Jinja2 + MySQL)

> A simple FastAPI + MySQL CRUD web app to manage student records. Built with Jinja2 templates and static CSS, it lets you view, add, edit, and delete students easily. Perfect for learning FastAPI, database integration, and building dynamic Python web apps.

---
## 📘 Overview
**Python MySQL CRUD** is a lightweight web application demonstrating Create, Read, Update, and Delete operations using **FastAPI**, **MySQL**, and **Jinja2 templates**.  
It provides a clean example of connecting FastAPI with a MySQL database while serving dynamic HTML pages styled with static CSS.

This project is ideal for learners and developers who want a practical template for database-driven FastAPI apps.

---

## ⚙️ Features
- View all student records  
- Fetch details of a single student by ID  
- Add, update, and delete student records  
- Organized folder structure using templates and static files  
- Simple UI built with HTML + CSS  

---

## 🏗️ Tech Stack
| Component | Technology |
|------------|-------------|
| Backend Framework | **FastAPI** |
| Database | **MySQL** |
| Template Engine | **Jinja2** |
| Styling | **CSS (Static Files)** |
| Server | **Uvicorn** |

---

,,,
> Tauheed Ahmad Shah   I am Tauheed Ahmad Shah.
,,,
## 🗂️ Folder Structure

python_mysql_crud/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI main application file
│ ├── db_config.py # Database connection and config
│ ├── models.py # Database models
│ ├── crud.py # CRUD operations
│ ├── static/ # Static files (CSS, JS)
│ │ └── style.css
│ └── templates/ # HTML templates
│ ├── base.html
│ ├── students.html
│ ├── add_student.html
│ ├── edit_student.html
│
├── database.sql # MySQL schema and sample data
├── requirements.txt # Dependencies
└── README.md # Project documentation
