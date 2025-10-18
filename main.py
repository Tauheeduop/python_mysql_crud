from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db import StudentDB

app = FastAPI()
db = StudentDB()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    students = db.get_all_students()
    # Convert to a format that matches what the template expects
    # students is a list of tuples: (student_id, first_name, email)
    formatted_students = [(student[0], student[1], student[2]) for student in students]
    return templates.TemplateResponse("students.html", {"request": request, "students": formatted_students})

@app.post("/add")
async def add_student(name: str = Form(...), email: str = Form(...)):
    db.add_student(name, email)
    return RedirectResponse(url="/", status_code=303)
@app.get("/delete/{student_id}")
async def delete_student(student_id: int):
    db.delete_student(student_id)
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit/{student_id}")
async def edit_student(request: Request, student_id: int):
    student = db.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    students = db.get_all_students()
    # Convert to a format that matches what the template expects
    formatted_students = [(student[0], student[1], student[2]) for student in students]
    return templates.TemplateResponse("students.html", {
        "request": request,
        "students": formatted_students,
        "edit_student": student
    })

@app.post("/update/{student_id}")
async def update_student(student_id: int, name: str = Form(...), email: str = Form(...)):
    db.update_student(student_id, name, email)
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)