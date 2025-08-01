from model.entity.user import *

name = "zahra"
family = "farzane"
password = "25845555"

name_validator(name)
family_validator(family)
password_validator(password)

user1 = User(1, name, family, "malihe@gmail.com", "khgffj", password, locked=True)

print(user1.name)
user1.password = "15484885"
print(user1.password)


