import sqlite3



class UserRepository:
    def connect(self):
        self.connection = sqlite3.connect("./model/repository/electronic_library_db")
        self.cursor = self.connection.cursor()

    def disconnect(self,commit=False):
        if commit:
            self.connection.commit()
        self.connection.close()
        self.connection.close()

    def save(self,user):
        self.connect()
        self.cursor.execute(
           """INSERT INTO USER 
                (user_id, name, family, email, username, password, locked)
             VALUES (?,?,?,?,?,?,?)""",
            [user.user_id, user.name, user.family,user.email, user.username, user.password, user.locked])
        self.disconnect(commit=True)
    def edit(self,user):
        self.connect()
        self.cursor.execute("update user set name=?, family=?, email=?, username=?, password=?, locked=? where user_id=?",
            [user.name, user.family, user.email, user.username, user.password, user.locked, user.user_id])
        self.disconnect(commit=True)
    def delete(self,user_id):
        self.connect()
        self.cursor.execute("delete from user where user_id=?", [user_id])
        self.disconnect(commit=True)
    def find_by_all(self):
        self.connect()
        self.cursor.execute("select * from USER")
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_user_id(self,user_id):
        self.connect()
        self.cursor.execute("select * from USER where user_id = ?",[user_id])
        user_list = self.cursor.fetchone()
        self.disconnect()
        return user_list
