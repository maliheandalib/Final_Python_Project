import sqlite3


def create_database():
    connection = sqlite3.connect("./model/repository/electronic_library_db")

    cursor = connection.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ADMIN(
                        admin_id    INTEGER PRIMERY KEY AUTOINCREMENT, 
                        name        TEXT NOT NULL, 
                        family      TEXT NOT NULL, 
                        username    TEXT NOT NULL, 
                        password    TEXT NOT NULL
                    )
                    """)

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS BOOK(
                        book_id   integer primary key AUTOINCREMENT, 
                        title     text not null, 
                        subject   text not null, 
                        author    text not null,
                        book_pdf  text not null
                    )
                    """)

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS USER(
                        user_id   integer primary key AUTOINCREMENT, 
                        name      text not null, 
                        family    text not null, 
                        email     tsxt not null, 
                        username  text not null unique, 
                        password  text not null,  
                        locked     tinyint default 0
                    )
                    """)

    connection.commit()

    cursor.close()

    connection.close()

