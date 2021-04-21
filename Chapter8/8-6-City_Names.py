def city_country(city, country):
    formatted_city = f"{city}, {country}"
    return formatted_city.title()

kansas_city = city_country('kansas city', 'united states')
rome = city_country('rome', 'italy')
paris = city_country('paris', 'france')

print(kansas_city)
print(rome)
print(paris)