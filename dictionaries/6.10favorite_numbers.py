favourite_numbers = {
    'alice': [3, 1, 5],
    'bob': [7],
    'carol': [12, 42],
    'dave': [10, 13],
    'eve': [5, 8, 21],
}

for name, numbers in favourite_numbers.items():
    if len(numbers) > 1:
        print(f"{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"{name.title()}'s favorite number is {numbers[0]}.")