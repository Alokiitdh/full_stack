from books import Books

class Member:
    def __init__(self, name):
        self.name = name
        self.books_record = []

    def __str__(self):
        if not self.books_record:
            return f"{self.name} does not borrowed any books"
        else:
            book_titles = ",".join([book.title for book in self.books_record])
            return f"{self.name} has borrowed:  {book_titles}"
    
    def borrow(self, book:Books):
        record = book.book_borrowed()
        if record == True:
            self.books_record.append(book)
            return f"{book.title} successufully borrowed"
        else:
            return f"{book.title} is not availabe "

    def return_book(self, book:Books):
        if book in self.books_record and book.book_return():
            self.books_record.remove(book)
            return f"{book.title} is returned successfully"
        else:
            return f"{self.name} can not return {book.title}"

