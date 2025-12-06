def city_country(city, country):
    "Formatted city country"
    msg = f"{city.title()}, {country.title()}"
    return msg


city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

