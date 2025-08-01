import re

def admin_id_validator(admin_id):
    if not (type(admin_id) == int and admin_id > 0):
        raise ValueError("Invalid Admin Id")

def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zآ-ی\s]{3,30}$", name)):
        raise ValueError("Invalid Name")

def family_validator(family):
    if not (type(family) == str and re.match(r"^[a-zآ-ی\s]{3,30}$", family)):
        raise ValueError("Invalid Family")

def username_validator(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z0-9_.\s]{8,20}$", username)):
        raise ValueError("Invalid Username")

def password_validator(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z0-9_.\s]{8,12}$", password)):
        raise ValueError("Invalid Password")