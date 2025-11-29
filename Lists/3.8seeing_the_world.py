places_to_see = ['america', 'saudi Arabia', 'dubai', 'germany', 'china']
print("Original list:", places_to_see)

sorted_places = sorted(places_to_see) # temporary sort
print("\nSorted list:", sorted_places)
print("Original list:", places_to_see)

sorted_places_reverse = sorted(places_to_see, reverse=True) # temporary reverse sort
print("\nReverse sorted list:", sorted_places_reverse)
print("Original list:", places_to_see)

places_to_see.reverse()  # permanent reverse
print("\nReversed list:", places_to_see)

places_to_see.reverse()  # reverse back to original
print("\nReversed back to original list:", places_to_see)

places_to_see.sort()  # permanent sort
print("\nPermanently sorted list:", places_to_see)

places_to_see.sort(reverse=True)  # permanent reverse sort
print("\nPermanently reverse sorted list:", places_to_see)

