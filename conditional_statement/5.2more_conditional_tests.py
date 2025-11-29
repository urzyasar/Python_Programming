first_string = "Hello"
second_string = "Hello"
print(first_string == second_string)
print(first_string != second_string)
second_string = "hello"
print(first_string == second_string)
print(first_string.lower() == second_string)

a=10
b=20
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

c = 15
print(a < c and c < b)
print(a < c or a < b)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print('cheese' not in requested_toppings)