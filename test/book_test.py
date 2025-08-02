from controller.book_controller import BookController
from model.entity.book import *

# book_id = 88
# title = "fffhhh"
# subject = "lssstttt"
#
# book_id_validator(book_id)
# title_validator(title)
# subject_validator(subject)
#
# book1 = Book(book_id, title, subject, "kjhggf")
#
# print(book1.subject)
# book1.author = "bbbbbjjjj"
# print(book1.author)

#book_repo = BookRepository()
#book_repo.save(book1)


#book_repo.edit(book1)

#book_repo.delete(1)


#print(book_repo.find_all())

book_controller = BookController()
print(book_controller.save(101, "raz","jgfgddt", "hyyfggf"))