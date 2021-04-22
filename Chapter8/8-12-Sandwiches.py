def sandwich(*ingredients):
    """Print supplied list of sandwich ingredients and a status message."""
    print("\nPreparing sandwich with the following ingredients:")
    for ingredient in ingredients:
        formatted_ingredient = ingredient.title()
        print(f" - {formatted_ingredient}")

sandwich('blueberries', 'bananas', 'toadstools')
sandwich('peanut butter', 'jelly')
sandwich('wood', 'fish', 'small rocks')