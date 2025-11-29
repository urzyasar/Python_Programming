people = ["Alice", "Bob", "Charlie", "David"]
print("Dear {0}, you are cordially invited to dinner.".format(people[0]))
print("Dear {0}, you are cordially invited to dinner.".format(people[1]))
print("Dear {0}, you are cordially invited to dinner.".format(people[2]))
print("Dear all, we have found a bigger dinner table, so more guests are invited!")
people.insert(0, "Eve") # beginning position
people.insert(2, "Frank") # middle position
people.append("Grace") # end position

print("Dear {0}, you are cordially invited to dinner.".format(people[0]))
print("Dear {0}, you are cordially invited to dinner.".format(people[1]))
print("Dear {0}, you are cordially invited to dinner.".format(people[2]))
print("Dear {0}, you are cordially invited to dinner.".format(people[3]))
print("Dear {0}, you are cordially invited to dinner.".format(people[4]))
print("Dear {0}, you are cordially invited to dinner.".format(people[5]))
print("Dear {0}, you are cordially invited to dinner.".format(people[6]))

print("\nUnfortunately, due to unforeseen circumstances, we can only invite two people for dinner.\n")
remove_guest = people.pop()
print("Dear {0}, we regret to inform you that we can no longer invite you to dinner.".format(remove_guest))
remove_guest = people.pop()
print("Dear {0}, we regret to inform you that we can no longer invite you to dinner.".format(remove_guest))
remove_guest = people.pop()
print("Dear {0}, we regret to inform you that we can no longer invite you to dinner.".format(remove_guest))
remove_guest = people.pop()
print("Dear {0}, we regret to inform you that we can no longer invite you to dinner.".format(remove_guest))
remove_guest = people.pop()
print("Dear {0}, we regret to inform you that we can no longer invite you to dinner.".format(remove_guest))

print("\nDear {0}, you are still invited to dinner.".format(people[0]))
print("Dear {0}, you are still invited to dinner.".format(people[1]))

del people[0]
del people[0]
print("\nFinal guest list:", people)

