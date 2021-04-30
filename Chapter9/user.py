class User:
    """Model a user."""
    
    def __init__(self, first_name, last_name, user_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.department = department

    def describe_user(self):
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"User Name: {self.user_name}")
        print(f"Department: {self.department}")
    
    def greet_user(self):
        print(f"\nHello, {self.first_name}!")
        print(f"Your user name is {self.user_name}.")

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