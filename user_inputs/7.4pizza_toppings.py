prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
topping = ""

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza!")
