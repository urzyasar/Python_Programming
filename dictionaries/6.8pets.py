pets = {
    'dog': {
        'type': 'canine',
        'owner': 'Alice',
    },
    'cat': {
        'type': 'feline',
        'owner': 'Bob',
    },
    'parrot': {
        'type': 'avian',
        'owner': 'Carol',
    },
}

for pet, details in pets.items():
    print(f"\nInformation about the {pet.title()}:")
    pet_type = details['type']
    owner = details['owner']
    
    print(f"Type: {pet_type}")
    print(f"Owner: {owner}")