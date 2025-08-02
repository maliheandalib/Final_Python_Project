import sqlite3


class BookRepository:
    def save(self,book):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO BOOK 
                (book_id, title, subject, author) 
            VALUES (?,?,?,?)""",
            [book.book_id, book.title, book.subject, book.author])
        connection.commit()
        cursor.close()
        connection.close()
    def edit(self,book):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("update book set book_id=?, title=?, subject=?, auther=?",
            [book.book_id, book.title, book.subject, book.author])
        connection.commit()
        cursor.close()
        connection.close()
    def delete(self,book_id):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("delete from book where book_id=?", [book_id])
        connection.commit()
        cursor.close()
        connection.close()
    def find_by_all(self,book):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from book")
        return self.cursor.fetchall()
        cursor.close()
        connection.close()

    def find_by_title(self,title):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from book where book_id = ?",[book_id])
        return self.cursor.fetchone()
        cursor.close()
        connection.close()

    def find_by_subject(self,subject ):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from book where subject = ?",[subject])
        return self.cursor.fetchone()
        cursor.close()
        connection.close()
