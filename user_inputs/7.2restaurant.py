message = "How many people are in your dinner group? "
people = int(input(message))
if people > 8:
    print("You'll have to wait for a table.")
else:    
    print("Your table is ready.")