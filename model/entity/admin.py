from model.tools.validation_admin import *

class Admin:
    def __init__(self, admin_id, name, family, username, password):
        self._admin_id = admin_id
        self._name = name
        self._family = family
        self._username = username
        self._password = password

    def full_name(self):
        return f"{self._name} {self._family}"

    def __repr__(self):
        return f"{self.full_name()}"

    @property
    def admin_id(self):
        return self._admin_id

    @admin_id.setter
    def admin_id(self, value):
        admin_id_validator(value)
        self._admin_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        family_validator(value)
        self._family = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        username_validator(value)
        self._username = value

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        password_validator(value)
        self._password = value




