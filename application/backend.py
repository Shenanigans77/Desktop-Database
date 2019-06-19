import sqlite3

def create():
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()
    except (ValueError, SyntaxError):
        print("oops")
    

def insert(title,author,year,isbn):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,:title,:author,:year,:isbn)", 
        {"title": title,"author": author,"year": year,"isbn":isbn})
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except (ValueError, SyntaxError):
        print("oops")
      

def delete(id):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=:id", {"id": id})
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except (ValueError, SyntaxError):
        print("oops")
    

def update(id,title,author,isbn,year):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=:title, author=:author, year=:year, isbn=:isbn WHERE id=:id", 
        {"title": title,"author": author,"year": year,"isbn":isbn,"id": id})
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except (ValueError, SyntaxError):
        print("oops")
    

def view():
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except (ValueError, SyntaxError):
        print("oops")
    

def search(title="",author="",year="",isbn=""):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=:title OR author=:author OR year=:year OR isbn=:isbn", 
        {"title": title,"author": author,"year": year,"isbn":isbn})
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except (ValueError, SyntaxError):
        print("oops")
    
#create()
#insert("Clean Code in Python","Mariano Anaya", 2018, 1788835832) 

#search("Clean Code")   
#sprint(view())