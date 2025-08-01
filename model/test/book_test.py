from model.entity.book import *

book_id = 88
title = "fffhhh"
subject = "lssstttt"

book_id_validator(book_id)
title_validator(title)
subject_validator(subject)

book1 = Book(book_id, title, subject, "kjhggf", "jkgh", "jkhgg")

print(book1.subject)
book1.author = "bbbbbjjjj"
print(book1.author)