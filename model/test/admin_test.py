from model.entity.admin import *

name = "farimah"
family = "attar"
password = "25845555"

name_validator(name)
family_validator(family)
password_validator(password)

admin1 = Admin(1, name, family, "mhfgfdd", password)

print(admin1.name)
admin1.password = "15484885"
print(admin1.password)



