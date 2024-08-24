
import classes

def load_data_from_files():
    # Load data from text files
    books = []
    users = []
    authors = []
    with open("books.txt", "r") as f:
        for line in f:
            title, author, genre, publication_date, availability = line.strip().split(",")
            books.append(classes.Book(title, author, genre, publication_date, availability))
    with open("users.txt", "r") as f:
        for line in f:
            name, library_id = line.strip().split(",")
            users.append(classes.User(name, library_id))
    with open("authors.txt", "r") as f:
        for line in f:
            name, biography = line.strip().split(",")
            authors.append(classes.Author(name, biography))
    return books, users, authors

def save_data_to_files(books, users, authors):
    # Save data to text files
    with open("books.txt", "w") as f:
        for book in books:
            f.write(f"{book.title},{book.author},{book.genre},{book.publication_date},{book.availability}\n")
    with open("users.txt", "w") as f:
        for user in users:
            f.write(f"{user.name},{user.library_id}\n")
    with open("authors.txt", "w") as f:
        for author in authors:
            f.write(f"{author.name},{author.biography}\n")
            return
        
def display_main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def display_book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def display_user_operations_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def display_author_operations_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a number.")


