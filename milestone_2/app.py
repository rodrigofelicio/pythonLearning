from utils import database

USER_CHOICE = """"
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book(book_name, book_author):  #ask for book name and author
    #database.add_book(book_name, book_author)  # list implementation of books database.py
    database.add_book(book_name, book_author)   # file implementation of books database.py


def prompt_list_books():  #show all the books in outr list
    # books = database.list_books()    # list implementation of books database.py
    books = database.get_all_books()   # file implementation of books database.py
    for book in books:
        #read = 'YES' if book['read'] else 'NO'        # list implementation of books database.py
        #read = 'YES' if book['read'] == '1' else 'NO' # csv file implementation of books database.py
        read = 'YES' if book['read'] else 'NO'         # json file implementation of books database.py
        print(f"This is {book['name']} by  {book['author']}, read: {read}")


def prompt_read_book(book_name):  #ask for book name and change it to "read" in our list
    # database.read_book(book_name)       # list implementation of books database.py
    database.mark_book_as_read(book_name) # file implementation of books database.py


def prompt_delete_book(book_name):  #ask for book name and remove book from list
    # database.delete_book(book_name) # list implementation of books database.py
    database.delete_book(book_name)   # file implementation of books database.py


def user_interaction(request_msg, inputs):
    user_input = input(request_msg).split(", ")
    book_info = []
    for an_input in range(inputs):
        book_info.append(user_input[an_input])
    
    user_input = 0
    return book_info


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            book_data = user_interaction("Please, provide Name and Author of the book: ", 2)
            prompt_add_book(book_data[0], book_data[1])
        elif user_input == 'l':
            prompt_list_books()
        elif user_input == 'r':
            book_data = user_interaction("Please, provide the Name of the book you've just finished reading: ", 1)
            prompt_read_book(book_data[0])            
        elif user_input == 'd':
            book_data = user_interaction("Please, provide the Name of the book to be deleted: ", 1)
            prompt_delete_book(book_data[0])            
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


menu()