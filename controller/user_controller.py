from model.entity.user import User
from model.repository.user_repository import UserRepository
class UserController:

    def save (self,user_id, name, family, email, username, password, locked):
        try:
            user = User(user_id, name, family, email, username, password, locked)
            user_repo =UserRepository()
            user_repo.save(user)
            return True, f"User saved{user}"
        except Exception as e:
            return False, f"error saving user{e}"

    def edit (self,user_id, name, family, email, username, password, locked):
        try:
            user = User(user_id, name, family, email, username, password, locked)
            user_repo = UserRepository()
            user_repo.edit(user)
            return True, f"User edited{user}"
        except Exception as e:
            return False, f"error editing user{e}"

    def delete (self,user_id):
        try:
            user_repo = UserRepository()
            user_repo.delete(user_id)
            return True, f"User removed{user_id}"
        except Exception as e:
            return False, f"error removing user{e}"

    def find_by_all(self,user):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_all()
        except Exception as e:
            return False,f"error find all user{e}"

    def find_by_user_id(self,user_id):
        try:
            user_repo = UserRepository()
            return True, user_repo.find_by_user_id(user_id)
        except Exception as e:
            return False, f"error find user user_id : user_id{user_id} -- Error {e}"