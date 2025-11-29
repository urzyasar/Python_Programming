persons = {
	"anand": {
		'first_name': 'John',
		'last_name': 'Doe',
		'age': 30,
		'city': 'New York'
	},
	"susan": {
		'first_name': 'Susan',
		'last_name': 'Smith',
		'age': 25,
		'city': 'Los Angeles'
	},
	"michael": {
		'first_name': 'Michael',
		'last_name': 'Johnson',
		'age': 40,
		'city': 'Chicago'
	}
}

for person, info in persons.items():
	print(f"\nInformation about {person.title()}:")
	full_name = f"{info['first_name']} {info['last_name']}"
	age = info['age']
	city = info['city']
	
	print(f"Full Name: {full_name}")
	print(f"Age: {age}")
	print(f"City: {city}")