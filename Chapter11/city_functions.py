def city_state(city, state, population=''):
    """Properly formate a supplied city and state."""
    if population:
        formatted_city = f"{city}, {state} - Population: {population}"
    else:
        formatted_city = f"{city}, {state}"
    return formatted_city.title()