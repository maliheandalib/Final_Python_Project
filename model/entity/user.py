from model.tools.validation_user import *


class User:
    def __init__(self, user_id, name, family, email, username, password, locked=False):
        self._user_id = user_id
        self._name = name
        self._family = family
        self._email = email
        self._username = username
        self._password = password
        self._locked = locked

    def full_name(self):
        return f"{self._name} {self._family}"

    def __repr__(self):
        return f"{self.full_name()}"

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        user_id_validator(value)
        self._user_id = value

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
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        email_validator(value)
        self._email = value

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

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        locked_validator(value)
        self._locked = value
