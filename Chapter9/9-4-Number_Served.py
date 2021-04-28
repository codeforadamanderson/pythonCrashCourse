class Restaurant:
    """Model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers

taco_bell = Restaurant('Taco Bell', 'Mexican-ish')
print(f"{taco_bell.restaurant_name}, a {taco_bell.cuisine_type} restaurant,")
print(f"has served {taco_bell.number_served} customers.")

taco_bell.set_number_served(3)
print(f"{taco_bell.restaurant_name}, a {taco_bell.cuisine_type} restaurant,")
print(f"has served {taco_bell.number_served} customers.")

taco_bell.increment_number_served(5)
print(f"{taco_bell.restaurant_name}, a {taco_bell.cuisine_type} restaurant,")
print(f"has served {taco_bell.number_served} customers.")