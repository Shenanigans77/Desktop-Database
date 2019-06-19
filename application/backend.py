import sqlite3

class Connector:

    def __init__(self,name):
        self.db_name = name

    def create_table(self): 
        command = "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
        return self.generic_connector(command)

    def search(self,title="",author="",year="",isbn=""):
        command = "SELECT * FROM book WHERE title=:title OR author=:author OR year=:year OR isbn=:isbn", {"title": title,"author": author,"year": year,"isbn":isbn}
        return self.generic_connector(command) 

    def generic_connector(self,command):
        #command = 
        print(command)
        try:
            conn = sqlite3.connect(self.db_name)
            cur = conn.cursor()
            cur.execute(command)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            return rows
        except (ValueError, SyntaxError):
            print("oops")


    def insert(self,title,author,year,isbn):
        try:
            title = str(title)
            author = str(author)            
            isbn = int(isbn)
            year = int(year)
            command = "INSERT INTO book VALUES(:title,:author,:year,:isbn)", {"title": title,"author": author,"year": year,"isbn":isbn} 
            print(command)
            return self.generic_connector(command)
        except ValueError:
            return 1
        
        
    def delete(self,id):
        try:
            id = int(id)
            command = "DELETE FROM book WHERE id=:id", {"id": id}
            return self.generic_connector(command)
        except ValueError:
            return 1
        

    def update(self,id,title,author,isbn,year):
        try:
            title = str(title)
            author = str(author)
            isbn = int(isbn)
            year = int(year)
            command = "UPDATE book SET title=:title, author=:author, year=:year, isbn=:isbn WHERE id=:id", {"title": title,"author": author,"year": year,"isbn":isbn,"id": id}
            return self.generic_connector(command)
        except ValueError:
            return 1
          

    def view(self):
        command = "SELECT * FROM book"
        return self.generic_connector(command)

link = Connector("books.db")
link.create_table()
link.insert("Clean Code in Python","Mariano Anaya", 2018, 1788835832)
print(link.view())