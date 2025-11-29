restaurant_menu = ('briyani', 'vegetable pulao', 'chicken curry', 'mutton curry', 'dal makhani')

for item in restaurant_menu:
    print(f"- {item.title()}")

#restaurant_menu[0] = 'fried rice'  # This will raise an error because tuples are immutable

new_menu = ('fried rice', 'paneer butter masala', 'chicken curry', 'mutton curry', 'dal makhani')
restaurant_menu = new_menu # reassigning a new tuple to the variable

print("\nUpdated Menu:")
for item in restaurant_menu:
    print(f"- {item.title()}")