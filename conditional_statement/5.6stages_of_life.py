age = 25

if age < 2:
    stage_of_life = "a baby"
elif age < 4:
    stage_of_life = "a toddler"
elif age < 13:
    stage_of_life = "a kid"
elif age < 20:
    stage_of_life = "a teenager"
elif age < 65:
    stage_of_life = "an adult"
else:
    stage_of_life = "an elder"

print(f"You are {stage_of_life}.")