"""""
Concerned with storing and retrieving books from SQLite database.
"""
from typing import List, Dict, Union
from .database_connection import DatabaseConnection

Book = [Dict[str, Union[str, int]]]

def create_book_table() -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text, author text, read integer)')


        
def add_book(name: str, author: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

    # This f'function approach to execute a SQL is note the recommended one
    # due to SQL Injection Attack
    # (example of SQL Statement: "--> ",0); DROP TABLE books; <--" ), 
    # because it is possible to run multiple SQL statements together
    #cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')

    #This below is the correct approach to execute a SQL STATEMENT
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)',  (name, author))


def get_all_books() -> List[Book]:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()    
        cursor.execute('SELECT * FROM books')
        # cursor.fetchall() will return a list of tuples like this: [(name, author, read), (name, author, read)]
        # so, using list comprehension... 
        books = [{ 'name': row[0], 'author': row[1], 'read': row[2] } for row in cursor.fetchall()]
    return books


def delete_book(name: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()    
    
        # Down below it is important the ',' after name in order to show python it is a tuple
        cursor.execute('DELETE FROM books name=?',(name,))   

def mark_book_as_read(name: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()    
    
        # Down below it is important the ',' after name in order to show python it is a tuple
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,)) 
        

############### The implementation below was created to consider json file handling.
###
###Concerned with storing and retrieving books from a json file
###
#
#"""""
#Concerned with storing and retrieving books from a json file.
#
#List of Dictionaries
#[
#    {
#        'name': 'Clean Code',
#        'authour': 'Robert',
#        'read': True
#    },
#    {
#        'name': 'Python 101',
#        'authour': 'Jose Salvatierra',
#        'read': False
#    }
#]
#"""   
#import json
#
#books_file = 'books.json'
#
#def create_book_table():
#    with open(books_file, 'w') as file:
#        json.dump([], file)
#
#def _save_all_books(books): 
#    with open(books_file, 'w') as file:
#        json.dump(books, file)
#
#
#def get_all_books():
#    with open(books_file, 'r') as file:
#        return json.load(file)
#    
#
#def add_book(name, author):
#    books = get_all_books()
#    books.append({'name': name, 'author': author, 'read': False})
#    _save_all_books(books)
#
#
#def delete_book(name):
#    books = get_all_books() 
#    books_to_keep = [book for book in books if book['name'] != name]
#    _save_all_books(books_to_keep)
#
#
#def mark_book_as_read(name):
#    books = get_all_books()
#    for book in books:
#        if book['name'] == name:
#            book['read'] = True
#    _save_all_books(books)
#
#



############### The implementation below was created to consider csv file handling.
###
###Concerned with storing and retrieving books from a csv file
###
#
#"""""
#Concerned with storing and retrieving books from a csv file.
#   
#Format of the csv file:
#name,author,read\n
#name,author,read\n
#name,author,read\n
#"""
#
#
#books_file = "books.txt"
#
#
#def create_book_table():
#    with open(books_file, 'w'):
#        pass # just to make sure the file is there
#
#
#def add_book(name, author):
#    with open('books.txt', 'a') as file:  # the 'a' means we will append the register at the EOF.
#        file.write(f'{name},{author},0\n')
#
#
#def get_all_books():
#    with open(books_file, 'r') as file:
#        lines = [line.strip().split(',') for line in file.readlines()] # [[name, author, read],[name, author, read]]
#
#    # [[name, author, read],[name, author, read]]
#    return [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]
#
#
## By name convention, this is a private function 
## (Python doesn't have this concept, that's why it starts with "_")
#def _save_all_books(books): 
#    with open(books_file, 'w') as file:
#        for book in books:
#            file.write(f"{book['name']}, {book['author']}, {book['read']}\n")
#
#
#def mark_book_as_read(name):
#    books = get_all_books()
#    for book in books:
#        if book['name'] == name:
#            book['read'] = '1'   
#    _save_all_books(books)
#
#
#def delete_book(name):
#    books = get_all_books() 
#    books_to_keep = [book for book in books if book['name'] != name]
#    _save_all_books(books_to_keep)
#






############### The implementation below was created to consider list management.
###
###Concerned with storing and retrieving books from a list.
###
#class BookNotFoundError(TypeError):
#    def __init__(self):
##        super().__init__('Book not Found, man!')
#
#books = []
#
#def list_books():
#    return(books)
#
#
#def find_book_by_name(book_name):
#    for book in books:
#        if books['name'] == book_name:
#            return book            
#
#def add_book(name, author):
#    books.append({'name': name, 'author': author, 'read': False})
#    print("Book added with success. Below is the list of your books:")
#    print(list_books())
#
#
#def read_book(book):
#    the_book = find_book_by_name(book)
#    the_book["read"] = True
#
#
#
####
##  Eu implementei esse método delete, mas não é uma boa prática
##  remover objetos enquanto realizamos uma interação sobre uma lista.
##  A boa prática está implementada no método seguinte usando list comprehension.
####
##def delete_book(book_name):
##    for book in books:
##        if book['name'] == book_name:
##            books.remove(book)
##            print("Book deleted successfully. Below is the list without it:")
##            print(list_books())
#
#
#def delete_book(name):
#    # Same variable, same global scope. 
#    # #This is needed because the books below is a variable created 
#    # in the local scope and we don't want another variable in the local scope, 
#    # we want to manage the global variable
#    global books 
#
#    books = [book for book in books if book['name'] != name] # add each book to new list if book['name'] != name
#    print("Book deleted successfully. Below is the list without it:")
#    print(list_books())
#