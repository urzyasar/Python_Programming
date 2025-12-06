
def make_sandwich(*toppings):
    """Adding the toppings user requested on sandwich"""
    for topping in toppings:
        print(topping)


make_sandwich('lettuce', 'tomato', 'bacon')
print('\n')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
print('\n')
make_sandwich('pepperoni')