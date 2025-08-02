import sqlite3

from model.entity import admin, user


class UserRepository:
    def save(self,user):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute(
           """INSERT INTO USER 
                (user_id, name, family,email, username, password, locked)
             VALUES (?,?,?,?,?,?,?)""",
            [user.user_id, user.name, user.family,user.email, user.username, user.password, user.locked])
        connection.commit()
        cursor.close()
        connection.close()
    def edit(self,user):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("update user set user_id=?, name=?, family=?, email=?, username=?, password=?",
            [user.user_id, user.name, user.family, user.email, user.username, user.password])
        connection.commit()
        cursor.close()
        connection.close()
    def delete(self,user_id):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("delete from user where user_id=?", [user_id])
        connection.commit()
        cursor.close()
        connection.close()
    def find_by_all(self,book):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from USER")
        return self.cursor.fetchall()
        cursor.close()
        connection.close()

    def find_by_user_id(self,user_id):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from USER where user_id = ?",[user_id])
        return self.cursor.fetchone()
        cursor.close()
        connection.close()
