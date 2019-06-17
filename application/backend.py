import sqlite3

class Connector:

    def __init__(self,name):
        self.db_name = name
        self.table = "book"

    def change_table(self,table):
        self.table = table

    def create_db(self):
        command = "CREATE TABLE IF NOT EXISTS ? (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)", (self.table)
        return self.generic_connector(command)

    def search(self,title="",author="",year="",isbn=""):
        command = "SELECT * FROM ? WHERE title=? OR author=? OR year=? OR isbn=?", (self.table,title,author,year,isbn)
        return self.generic_connector(command) 

    def generic_connector(self,command):
        try:
            conn = sqlite3.connect(self.db_name)
            cur = conn.cursor()
            cur.execute(command)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            return rows
        except ValueError:
            pass
        

    def insert(self,title,author,isbn,year):
        try:
            title = str(title)
            author = str(author)            
            isbn = int(isbn)
            year = int(year)
            command = "INSERT INTO ? VALUES(?,?,?,?)", (self.table,title,author,isbn,year) 
            return self.generic_connector(command)
        except ValueError:
            pass
        
        
    def delete(self, id):
        try:
            id = int(id)
            command = "DELETE FROM ? WHERE id=?", (self.table,id)
            return self.generic_connector(command)
        except ValueError:
            pass
        

    def update(self,table,title,author,isbn,year):
        try:
            title = str(title)
            author = str(author)
            isbn = int(isbn)
            year = int(year)
            command = "UPDATE ? SET ", (self.table,title,author,isbn,year)
            return self.generic_connector(command)
        except ValueError:
            pass
          

    def view(self):
        command = "SELECT * FROM ?", (self.table)
        return self.generic_connector(command)