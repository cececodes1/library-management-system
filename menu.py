

import classes
import user_interactions
def load_data_from_files():
    books = []
    users = []
    authors = []
    # Load data from files and append to the lists
    return books, users, authors

def save_data_to_files(books, users, authors):
    pass
def main():
    books, users, authors = load_data_from_files()


    while True:
        user_interactions.display_main_menu()
        choice = user_interactions.get_user_input("Enter your choice: ")

        if choice == 1:
            # Book Operations
            while True:
                user_interactions.display_book_operations_menu()
                book_choice = user_interactions.get_user_input("Enter your choice: ")

                if book_choice == 1:
                    # Add a new book
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    genre = input("Enter genre: ")
                    publication_date = input("Enter publication date: ")
                    books.append(classes.Book(title, author, genre, publication_date))

                elif book_choice == 2:
                    # Borrow a book
                    book_title = input("Enter book title: ")
                    for book in books:
                        if book.title == book_title:
                            book.borrow()
                            print("Book borrowed successfully!")
                            break
                    else:
                        print("Book not found.")

                elif book_choice == 3:
                    # Return a book
                    book_title = input("Enter book title: ")
                    for book in books:
                        if book.title == book_title:
                            book.return_book()
                            print("Book returned successfully!")
                            break
                    else:
                        print("Book not found.")

                elif book_choice == 4:
                    # Search for a book
                    book_title = input("Enter book title: ")
                    for book in books:
                        if book.title == book_title:
                            print(f"Title: {book.title}")
                            print(f"Author: {book.author}")
                            print(f"Genre: {book.genre}")
                            print(f"Publication Date: {book.publication_date}")
                            print(f"Availability: {'Available' if book.availability else 'Not Available'}")
                            break
                        else:
                            print("Book not found.")

                    # Display all books
                elif book_choice == 5:
                    for book in books:
                        print(f"Title: {book.title}")
                        print(f"Author: {book.author}")
                        print(f"Genre: {book.genre}")
                        print(f"Publication Date: {book.publication_date}")
                        print(f"Availability: {'Available' if book.availability else 'Not Available'}")
                        print()

                else:
                    print("Invalid choice. Please try again.")
                    break

                if choice == 2:
            # User Operations
                    while True:
                        user_interactions.display_user_operations_menu()
                user_choice = user_interactions.get_user_input("Enter your choice: ")

                if user_choice == 1:
                    # Add a new user
                    name = input("Enter user name: ")
                    library_id = input("Enter library ID: ")
                    users.append(classes.User(name, library_id))
                    print("User added successfully!")

                elif user_choice == 2:
                    # View user details
                    user_name = input("Enter user name: ")
                    for user in users:
                        if user.name == user_name:
                            print(f"Name: {user.name}")
                            print(f"Library ID: {user.library_id}")
                            break
                    else:
                        print("User not found.")

                elif user_choice == 3:
                    # Display all users
                    for user in users:
                        print(f"Name: {user.name}")
                        print(f"Library ID: {user.library_id}")
                        print()

                else:
                    print("Invalid choice. Please try again.")
                    break

        elif choice == 3:
            # Author Operations
            while True:
                user_interactions.display_author_operations_menu()
                author_choice = user_interactions.get_user_input("Enter your choice: ")

                if author_choice == 1:
                    # Add a new author
                    name = input("Enter author name: ")
                    biography = input("Enter author biography: ")
                    authors.append(classes.Author(name, biography))
                    print("Author added successfully!")

                elif author_choice == 2:
                    # View author details
                    author_name = input("Enter author name: ")
                    for author in authors:
                        if author.name == author_name:
                            print(f"Name: {author.name}")
                            print(f"Biography: {author.biography}")
                            break
                    else:
                        print("Author not found.")

                elif author_choice == 3:
                    # Display all authors
                    for author in authors:
                        print(f"Name: {author.name}")
                        print(f"Biography: {author.biography}")
                        print()

                else:
                    print("Invalid choice. Please try again.")

        elif choice == 4:
                #Quit
            save_data_to_files(books, users, authors)
            print("Goodbye!")

if __name__ == "__main__":
    main()