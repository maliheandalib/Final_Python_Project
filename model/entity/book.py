from model.tools.validation_book import *

class Book:
    def __init__(self, book_id, title, subject, author, pdf_path, upload_date):
        self._book_id = book_id
        self._title = title
        self._subject = subject
        self._author = author


    def __repr__(self):
        return f"{self.__dict__}"

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        book_id_validator(value)
        self._book_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        title_validator(value)
        self._title= value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        subject_validator(value)
        self._subject = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        author_validator(value)
        self._author = value



