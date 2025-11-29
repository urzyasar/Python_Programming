people = ["Alice", "Bob", "Charlie", "David"]
print("Dear {0}, you are cordially invited to dinner.".format(people[0]))
print("Dear {0}, you are cordially invited to dinner.".format(people[1]))
print("Dear {0}, you are cordially invited to dinner.".format(people[2]))
not_coming = people[3]
print("Unfortunately, {0} can't make it to the dinner.".format(not_coming))
people[3] = "Eve"
print("Dear {0}, you are cordially invited to dinner.".format(people[3]))
