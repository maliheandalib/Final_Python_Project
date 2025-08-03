from model.entity.admin import Admin
from model.repository.admin_repository import AdminRepository


class AdminController:
    def save(self, admin_id, name, family, username, password):
        try:
            admin = Admin(admin_id, name, family, username, password)
            admin_repo = AdminRepository()
            admin_repo.save(admin)
            return True, f"Admin saved{admin}"
        except Exception as e:
            return False, f"error saving admin{e}"

    def edit(self, admin_id, name, family, username, password):
        try:
            admin = Admin(admin_id, name, family, username, password)
            admin_repo = AdminRepository()
            admin_repo.edit(admin)
            return True, f"Admin edited{admin}"
        except Exception as e:
            return False, f"error editing admin{e}"

    def delete(self, admin_id):
        try:
            admin_repo = AdminRepository()
            admin_repo.delete(admin_id)
            return True, f"Admin removed{admin_id}"
        except Exception as e:
            return False, f"error removing admin{e}"

    def find_by_all(self, admin):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_by_all(admin)
        except Exception as e:
            return False,f"error find all admin{e}"


    def find_by_admin_id(self, admin_id):
        try:
            admin_repo = AdminRepository()
            return True, admin_repo.find_by_admin_id(admin_id)
        except Exception as e:
            return False, f"error find admin admin_id : admin_id{admin_id} -- Error {e}"