cities = {
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'Known as the City of Light',
    },
    'itali': {
        'country': 'italy',
        'population': 2873000,
        'fact': 'Famous for its ancient history and architecture',
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'The largest metropolitan area in the world',
    },
}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    
    print(f"\nInformation about {city.title()}:")
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")