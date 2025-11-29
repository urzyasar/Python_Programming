mountains = ['everest', 'k2', 'kangchenjunga', 'lhotse', 'makalu']
print(f"The top 5 mountains in the world are: {mountains}")

print("The tallest mountain in the world is:", mountains[0].title())

sorted_mountains = sorted(mountains)
print(f"\nHere is the sorted list of mountains: {sorted_mountains}")
print(f"\nThe original list of mountains is still intact: {mountains}")

sorted_mountains_reverse = sorted(mountains, reverse=True)
print(f"\nHere is the reverse sorted list of mountains: {sorted_mountains_reverse}")
print(f"\nThe original list of mountains is still intact: {mountains}")

mountains.sort()
print(f"\nHere is the permanently sorted list of mountains: {mountains}")

mountains.sort(reverse=True)
print(f"\nHere is the permanently reverse sorted list of mountains: {mountains}")

mountains.reverse()
print(f"\nHere is the list of mountains after reversing the order: {mountains}")

print("The number of mountains in the list is:", len(mountains))

print("The last mountain in the list is:", mountains.pop().title())
print("The remaining mountains are:", mountains)

third_mountain = mountains.pop(2)
print(f"The third mountain removed from the list is: {third_mountain.title()}")
print("The remaining mountains are:", mountains)

mount_everest = 'everest'
mountains.remove(mount_everest)
print(f"\nAfter removing {mount_everest.title()}, the remaining mountains are: {mountains}")

del mountains[0]
print(f"\nAfter deleting the first mountain, the remaining mountains are: {mountains}")
