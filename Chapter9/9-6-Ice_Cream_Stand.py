class Restaurant:
    """Model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

class IceCreamStand(Restaurant):
    """Model a child of Restaurant, ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'coffee']

    def list_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()} ")

stand1 = IceCreamStand('Silas and Maddy', 'Ice Cream')
stand1.list_flavors()