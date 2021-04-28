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

user1 = User('Joe', 'Shmoe', 'jshmoe', 'Sales')
user2 = User('Jane', 'Doe', 'jdoe', 'Marketing')
user3 = User('Steve', 'Herobrine', 'sherobrine', 'Engineering')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()