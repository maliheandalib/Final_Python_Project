from controller.user_controller import UserController
from model.entity.user import *

# name = "zahra"
# family = "farzane"
# password = "25845555"
#
# name_validator(name)
# family_validator(family)
# password_validator(password)
#
# user1 = User(1, name, family, "malihe@gmail.com", "khgffj", password, locked=True)
#
# print(user1.name)
# user1.password = "15484885"
# print(user1.password)


#user_repo = UserRepository()
#user_repo.save(user1)


#user_repo.edit(user1)

#user_repo.delete(1)


#print(user_repo.find_all())

user_controller = UserController()
print(user_controller.save(1, "mona","azary", "mona66@gmail.com", "mona123", 12345678, True))


