import sqlite3

class Connector:

    def __init__(self,name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        try:
            self.cur.execute("INSERT INTO book VALUES(NULL,:title,:author,:year,:isbn)", 
            {"title": title,"author": author,"year": year,"isbn":isbn})
            rows = self.cur.fetchall()
            self.conn.commit()
            return rows
        except (ValueError, SyntaxError):
            print("oops")
        

    def delete(self,id):
        try:
            self.cur.execute("DELETE FROM book WHERE id=:id", {"id": id})
            rows = self.cur.fetchall()
            self.conn.commit()
            return rows
        except (ValueError, SyntaxError):
            print("oops")
        

    def update(self,id,title,author,year,isbn):
        try:
            self.cur.execute("UPDATE book SET title=:title, author=:author, year=:year, isbn=:isbn WHERE id=:id", 
            {"title": title,"author": author,"year": year,"isbn":isbn,"id": id})
            rows = self.cur.fetchall()
            self.conn.commit()
            return rows
        except (ValueError, SyntaxError):
            print("oops")
        

    def view(self):
        try:
            self.cur.execute("SELECT * FROM book")
            rows = self.cur.fetchall()
            self.conn.commit()
            return rows
        except (ValueError, SyntaxError):
            print("oops")
        

    def search(self,title="",author="",year="",isbn=""):
        try:
            self.cur.execute("SELECT * FROM book WHERE title=:title OR author=:author OR year=:year OR isbn=:isbn", 
            {"title": title,"author": author,"year": year,"isbn":isbn})
            rows = self.cur.fetchall()
            self.conn.commit()
            return rows
        except (ValueError, SyntaxError):
            print("oops")

    def __del__(self):
        self.conn.close()