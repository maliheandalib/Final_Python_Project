import sqlite3

class AdminRepository:
    def save(self,admin):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO ADMIN 
                    ( admin_id, name, family, username, password) 
                VALUES (?,?,?,?,?)""",
            [admin.admin_id, admin.name, admin.family, admin.username, admin.password])
        connection.commit()
        cursor.close()
        connection.close()

    def edit(self,admin):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("update admin set admin_id=?, name=?, family=?, username=?, password=?",
                       [admin.admin_id, admin.name, admin.family, admin.username, admin.password])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self,admin_id):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("delete from admin where admin_id=?", [admin_id])
        connection.commit()
        cursor.close()
        connection.close()

    def find_by_all(self,admin):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from ADMIN")
        return self.cursor.fetchall()
        cursor.close()
        connection.close()


    def find_by_admin_id(self,admin_id):
        connection = sqlite3.connect("./model/repository/electronic_library_db")
        cursor = connection.cursor()
        cursor.execute("select * from ADMIN where admin_id = ?",[admin_id])
        return self.cursor.fetchone()
        cursor.close()
        connection.close()
