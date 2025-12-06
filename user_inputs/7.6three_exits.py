prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
topping = ""

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza!")

prompt = "\n2. What topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
topping = ""

flag = True
while flag:
    topping = input(prompt)
    if topping.lower() == 'quit':
        flag = False
        continue
    print(f"Adding {topping} to your pizza!")


