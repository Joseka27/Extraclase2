from model.user import User

class UserService:
    def __init__(self):
        # Simulamos un almacenamiento en memoria usando un diccionario
        self.users = {}
        self.next_user_id = 1

    def create_user(self, name, email):
        user_id = self.next_user_id
        self.next_user_id += 1
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)