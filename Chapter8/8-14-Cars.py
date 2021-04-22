def car(manufacturer, model, **cars):
    """Add supplied car information to a dictionary."""
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    return cars

car1 = car(
    manufacturer='subaru', model='outback', color='blue', tow_package=True)

print(car1)