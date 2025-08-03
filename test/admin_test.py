from controller.admin_controller import AdminController
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



#admin_repo = AdminRepository()
#admin_repo.save(admin1)


#admin_repo.edit(admin1)

#admin_repo.delete(1)


#print(admin_repo.find_all())

admin_controller = AdminController()
print(admin_controller.save(1, "mona","azary", "mona123", "12358521"))