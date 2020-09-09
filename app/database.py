import sqlite3
connection=sqlite3.connect("books.sqlite3")
cursor=connection.cursor()
sql_query='''CREATE TABLE bb(
    id integer PRIMARY KEY,
    book_name char(100) NOT NULL,
    author_name char(100) NOT NULL,
    genre char(50) NOT NULL,
    publisher char(50) NOT NULL  
)'''

cursor.execute(sql_query)