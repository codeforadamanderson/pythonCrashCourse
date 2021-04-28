class Restaurant:
    """Model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

olive_garden = Restaurant('Olive Garden', 'Italian-ish')
panda_express = Restaurant('Panda Express', 'Chineese-ish')
mi_ranchito = Restaurant('Mi Ranchito', 'Mexixan-ish')

olive_garden.describe_restaurant()
panda_express.describe_restaurant()
mi_ranchito.describe_restaurant()