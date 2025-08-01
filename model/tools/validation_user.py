import re

def user_id_validator(user_id):
    if not (type(user_id) == int and user_id > 0):
        raise ValueError("Invalid User Id")

def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Zآ-ی\s]{3,30}$", name)):
        raise ValueError("Invalid Name")

def family_validator(family):
    if not (type(family) == str and re.match(r"^[a-zA-Zآ-ی\s]{3,30}$", family)):
        raise ValueError("Invalid Family")

def email_validator(email):
    if not (type(email) == str and re.match(r"^[a-z][a-z0-9_.]{1,49}@(gmail|yahoo)\.com$",email)):
        raise ValueError("Invalid Email")

def username_validator(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z0-9_.\s]{8,20}$", username)):
        raise ValueError("Invalid Username")

def password_validator(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z0-9_.\s]{8,12}$", password)):
        raise ValueError("Invalid Password")

def locked_validator(locked):
    if not type(locked) == bool:
        raise ValueError("Invalid Locked")
