# from typing import List
# from fastapi.responses import HTMLResponse
# from fastapi import FastAPI, Path, Body ,Request
# from pydantic import BaseModel, Field
# from fastapi.templating import Jinja2Templates
#
# app = FastAPI()
#
# # class Student(BaseModel):
#     id: int
#     name: str = Field(None, title="name of student", max_length=10)
#     subject: List[str] = []
import shutil

# @app.get("/")
# async def root():
#     return {"message": "hello world"}
#
#
# @app.get("/hello/{name}")
# async def root(name: str = Path(..., min_length=3, max_length=10),
#                age: int = Path(..., ge=1, le=100)):
#     return {"name": name, "age": age}

# @app.post("/students/")
# async def student_data(s1:Student):
#     return s1
# @app.get("/hello/")
# async def hello():
#     ret = '''<html>
# <body>
# <h2>Hello World!</h2>
# </body>
# </html>'''
#     return HTMLResponse(content=ret)
#
# templates = Jinja2Templates(directory="templates")
#
#
# @app.get("/hello/", response_class=HTMLResponse)
# async def hello(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})

# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
#
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
#
# # @app.get("/hello/{name}", response_class=HTMLResponse)
# # async def hello(request: Request, name: str):
# #     return templates.TemplateResponse("login.html", {"request": request, "name": name})
#
# @app.get("/login/", response_class=HTMLResponse)
# async def login(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})
#
#
# # @app.post("/submit/")
# # async def submit(name: str = Form(...), password: str = Form(...)):
# #     return {"username": name ,
# #             "password": password}
#
# class User(BaseModel):
#     username: str
#     password: int
#
#
# @app.post("/submit/")
# async def submit(nm: str = Form(...), pwd: int = Form(...)):
#     return User(username=nm, password=pwd)

# from fastapi import FastAPI, Request, UploadFile, File
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
#
# templates = Jinja2Templates(directory="templates")
#
#
# @app.get("/upload/", response_class=HTMLResponse)
# async def upload(request: Request):
#     return templates.TemplateResponse("uploadfile.html", {"request": request})
#
#
# @app.post("/uploader/")
# async def create_upload_file(file: UploadFile = File(...)):
#     with open("destination.png", "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {"filename": file.filename}
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

app = FastAPI()

data = []


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str


@app.post("/book")
async def add_book(b1: Book):
    data.append(b1.dict())
    return data


@app.get("/list")
async def list_books():
    return data


@app.get("/book/{id}")
async def get_book(id: int):
    id = id - 1
    return data[id]


@app.put("/book/{id}")
async def update_book(id: int, book: Book):
    data[id - 1] = book
    return data


@app.delete("/book/{id}")
async def delete_book(id: int):
    data.pop(id - 1)
    return data
