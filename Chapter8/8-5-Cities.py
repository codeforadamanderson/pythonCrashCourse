def describe_city(city, country='Canada'):
    """Prints a message about a city and country."""
    print(f"\n{city.title()} is in {country.title()}")

describe_city('Dublin', 'Ireland')

describe_city('Ontario')

describe_city('Mexico City', 'Mexico')