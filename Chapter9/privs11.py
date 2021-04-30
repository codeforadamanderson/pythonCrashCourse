from user11 import User

class Privileges:
    """Model a set of privileges for a user."""

    def __init__(self, privileges = [
        'can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")

class Admin(User):
    """Model a type of user, admin."""

    def __init__(self, first_name, last_name, user_name, department):
        super().__init__(first_name, last_name, user_name, department)
        self.privileges = Privileges()