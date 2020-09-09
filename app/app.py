from flask import Flask, jsonify, request,redirect
import sqlite3
app=Flask('__name__')
app.config["debug"]=True

@app.route('/')
def greet():
    return "<h1>HelloWorld</h1>"
def dbConnection():
    connection=None
    try:
        connection=sqlite3.connect("books.sqlite3")
    except:
        print(sqlite3.Error)
    return connection     

@app.route('/books/create',methods=['POST'])
def createBook():
    connection=dbConnection()
    cursor=connection.cursor()
    book_id=request.form['id']
    book_name=request.form['book_name']
    author_name=request.form['author_name']
    genre=request.form['genre']
    publisher=request.form['publisher']
    cursor.execute('''INSERT INTO bb(id,book_name,author_name,genre,publisher)
    VALUES(?,?,?,?,?)''',(book_id,book_name,author_name,genre,publisher))
    connection.commit()
    print("BUILD SUCCESS",201)
    return redirect('/');
    