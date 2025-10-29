from books import Books
from member import Member

class Library:
    def __init__(self, lib_name):
        self.lib_name = lib_name
        self.books_record = []
        self.member_record = []
    
    def __str__(self):
        return f"The {self.lib_name} have {len(self.books_record)} books and {len(self.member_record)} members"
    
    def add_books(self, book:Books):
        self.books_record.append(book)
        return f"{book.title} added succesfully"

    def add_member(self, mem:Member):
        self.member_record.append(mem)
        return f"{mem.name} added succesfully"

    def list_books(self):
        if not self.books_record:
            return "No books areavailable"
        else:
            return "\n".join([str(book) for book in self.books_record])

    def list_members(self):
        if not self.member_record:
            return "No member is available"
        else:
            return "\n".join([str(mem) for mem in self.member_record])
