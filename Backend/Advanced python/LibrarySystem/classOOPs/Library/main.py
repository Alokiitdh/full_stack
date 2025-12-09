from fastapi import FastAPI
from library import Library
from member import Member
from books import Books
from pydantic import BaseModel


class BookSchema(BaseModel):
    title:str
    author: str
    year: str

class MemberSchema(BaseModel):
    name: str

class LibName(BaseModel):
    lib_name: str

class Borrow(BaseModel):
    title: str
    member: str

app = FastAPI(title="Library API")

# Global Variable
library : Library | None = None

@app.post("/Library Name")
def Lib_name(book_schmea: LibName):
    global library
    library = Library(book_schmea.lib_name)
    return library.lib_name


@app.post("/Add books")
def Add_books(book_schmea: BookSchema):
    new_book = Books(
        title=book_schmea.title,
        author=book_schmea.author,
        year=book_schmea.year
    )
    added_book = library.add_books(book=new_book)
    return added_book

@app.post("/Members")
def Add_members(mem_schema:MemberSchema):
    new_member = Member(
        name=mem_schema.name
    )
    added_member = library.add_member(mem=new_member)

    return added_member

@app.get("/Books Record")
def Book_record():
    return library.list_books()

@app.get("/Member Record")
def Member_record():
    return library.list_members()

# @app.post("/Borrow")
# def Borrow()
    

# @app.post("/Return")
# pass
