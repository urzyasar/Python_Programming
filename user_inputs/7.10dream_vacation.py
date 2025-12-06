# https://github.com/ehmatthes/pcc_3e/blob/main/solution_files/chapter_07/dream_vacation.py
name_prompt = "What is your name? "
place_prompt = "\nIf you could one place in the world, Where would you like to go?: "

responses = {}

poll_active = True
while poll_active:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] =  place

    poll_continue = input("Would you like to continue the poll for others[Yes/No]: ")
    if poll_continue == 'Yes':
        continue
    else:
        break

print('\n')
for name, place in responses.items():
    print(f"{name.title()} would love to go {place.title()}")
    