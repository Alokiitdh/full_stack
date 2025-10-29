class Books:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title 
        self.author = author
        self.year = year
        self.is_available = True # Always consider the default as availabe wheen a book is added

    def __str__(self): ## gives the human readable representation of the object
        
        if self.is_available:
            status = "Available"
        else:
            status = "Borrowed"
        return f"The book '{self.title}' written by '{self.author}' is '{status}'"
            
        
    def book_borrowed(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def book_return(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False
    


