from model.entity.book import Book
from model.repository.book_repository import BookRepository


class BookController:


    def save(self,book_id, title, subject, author, book_pdf):
        try:
            book = Book(book_id, title, subject, author, book_pdf)
            book_repo = BookRepository()
            book_repo.save(book)
            return True, f"Book saved{book}"
        except Exception as e:
            return False, f"error saving book{e}"


    def edit(self, book_id, title, subject, author, book_pdf):
        try:
            book = Book(book_id, title, subject, author, book_pdf)
            book_repo = BookRepository()
            book_repo.edit(book)
            return True, f"Admin edited{book}"
        except Exception as e:
            return False, f"error editing book{e}"

    def delete(self, book_id):
        try:
            book_repo = BookRepository()
            book_repo.delete(book_id)
            return True, f"User removed{book_id}"
        except Exception as e:
            return False, f"error removing book{e}"

    def find_by_all(self, book):
        try:
            book_repo = BookRepository()
            return True, book_repo.find_by_all(book)
        except Exception as e:
            return False,f"error find all book{e}"

    def find_by_title(self, title):
        try:
            book_repo = BookRepository()
            return True, book_repo.find_by_title(title)
        except Exception as e:
            return False, f"error find book title : title{title} -- Error {e}"
    def find_by_subject(self, subject):
        try:
            book_repo = BookRepository()
            return True, book_repo.find_by_subject(subject)
        except Exception as e:
            return False, f"error find book subject : subject{subject} -- Error {e}"