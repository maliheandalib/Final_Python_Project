import sqlite3

class AdminRepository:
    def connect(self):
        self.connection = sqlite3.connect("./model/repository/electronic_library_db")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.connection.close()
        self.connection.close()

    def save(self,admin):
        self.connect()
        self.cursor.execute(
            """INSERT INTO ADMIN 
                    ( admin_id, name, family, username, password) 
                VALUES (?,?,?,?,?)""",
            [admin.admin_id, admin.name, admin.family,admin.username, admin.password])
        self.disconnect(commit=True)
    def edit(self,admin):
        self.connect()
        self.cursor.execute("update ADMIN set admin_id=?, name=?, family=?, username=?, password=? where admin_id=?",
                            [admin.admin_id, admin.name,admin.family,admin.username, admin.password]
                            )
        self.disconnect(commit=True)

    def delete(self,admin_id):
        self.connect()
        self.cursor.execute("delete from ADMIN where admin_id=?", [admin_id])
        self.disconnect(commit=True)

    def find_by_all(self):
        self.connect()
        self.cursor.execute("select * from ADMIN")
        admin_list = self.cursor.fetchall()
        self.disconnect()
        return admin_list


    def find_by_admin_id(self,admin_id):
        self.connect()
        self.cursor.execute("select * from ADMIN where admin_id = ?",[admin_id])
        admin_list = self.cursor.fetchone()
        self.disconnect()
        return admin_list
