
class Book:
    def __init__(self, title, author, genre, publication_date, availability=True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = availability
        self.__borrowed_by = None
        self.__due_date = None

    
    def title(self):
        return self.__title

    
    def author(self):
        return self.__author

    
    def genre(self):
        return self.__genre

    
    def publication_date(self):
        return self.__publication_date

    
    def availability(self):
        return self.__availability

    def borrow(self):
        self.__availability = False

    def return_book(self):
        self.__availability = True

    def __borrowed_by(self):
        return self.__borrowed_by
    
    def __due_date(self):
        return self.__due_date


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
        self.__reserved_books = []
        self.__fines = 0

    
    def name(self):
        return self.__name

    
    def library_id(self):
        return self.__library_id

    
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        self.__borrowed_books.remove(book_title)

    def __reserved_books(self):
        return self.__reserved_books
    def reserve_book(self, book_title):
        self.__reserved_books.append(book_title)    
    def __fines(self):
        return self.__fines


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    
    def name(self):
        return self.__name

    
    def biography(self):
        return self.__biography


    
