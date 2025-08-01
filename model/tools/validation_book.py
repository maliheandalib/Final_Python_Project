import re

def book_id_validator(book_id):
    if not (type(book_id) == int and book_id > 0):
        raise ValueError("Invalid Book Id")

def title_validator(title):
    if not (type(title) == str and re.match(r"^[آ-یa-zA-Z0-9_.\s]{3,30}$", title)):
        raise ValueError("Invalid Title")

def subject_validator(subject):
    if not (type(subject) == str and re.match(r"^[آ-یa-zA-Z0-9_.\s]{3,30}$", subject)):
        raise ValueError("Invalid Subject")

def author_validator(author):
    if not (type(author) == str and re.match(r"^[آ-یa-zA-Z\s]{3,30}$", author)):
        raise ValueError("Invalid Author")