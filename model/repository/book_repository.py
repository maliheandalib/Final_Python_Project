import sqlite3


class BookRepository:
    def connect(self):
        self.connection = sqlite3.connect("./model/repository/electronic_library_db")
        self.cursor = self.connection.cursor()

    def disconnect(self,commit=False):
        if commit:
            self.connection.commit()
        self.connection.close()
        self.connection.close()

    def save(self,book):
        self.connect()
        self.cursor.execute(
            """INSERT INTO BOOK 
                (book_id, title, subject, author, book_pdf) 
            VALUES (?,?,?,?,?)""",
            [book.book_id, book.title, book.subject, book.author, book.book_pdf])
        self.disconnect(commit=True)
    def edit(self,book):
        self.connect()
        self.cursor.execute("update BOOK set book_id=?, title=?, subject=?, author=?, book_pdf=? where book_id=?",
            [book.book_id, book.title, book.subject, book.author, book.book_pdf])
        self.disconnect(commit=True)
    def delete(self,book_id):
        self.connect()
        self.cursor.execute("delete from BOOK where book_id=?", [book_id])
        self.disconnect(commit=True)
    def find_by_all(self):
        self.connect()
        self.cursor.execute("select * from book")
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list
    def find_by_title(self,title):
        self.connect()
        self.cursor.execute("select * from BOOK where title = ?",[title])
        user_list = self.cursor.fetchone()
        self.disconnect()
        return user_list
    def find_by_subject(self,subject ):
        self.connect()
        self.cursor.execute("select * from BOOK where subject = ?",[subject])
        user_list = self.cursor.fetchone()
        self.disconnect()
        return user_list
