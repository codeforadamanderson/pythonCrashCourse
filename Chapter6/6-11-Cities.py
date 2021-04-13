cities = {
    'london': {
        'country': 'united kingdom',
        'population': 'tonnes',
        'fact': 'Very British'
    },
    'paris': {
        'country': 'france',
        'population': 'loads',
        'fact': 'Has French people'
    },
    'dallas': {
        'country': 'united states of america',
        'population': 'lots',
        'fact': 'Does not have proper BBQ'
    },
}

for city, information in cities.items():
    print(f"\n{city.title()}:")
    country = information['country']
    population = information['population']
    fact = information['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")