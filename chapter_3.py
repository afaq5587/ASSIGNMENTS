# EXERCISE 3.1....

names :list[str] = ["danish" , "ali" , "aslam", "usama"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Exercise 3.2....-------------------------------------------------------------------------

names :list[str] = ["danish" , "ali" , "aslam", "usama"]
for i in names:
    print(f"{i.title()} you are invited in mehandi function")

# Exercise 3.3....

transports : list[str] = ["bus" , "car" , "bike" , "train"]
for i in transports:
    print(f"I would like to travel in {i}.")

# ----------------------------------------------------------------------------------------------------
# Exercise 3.4....

guests = ['ali', 'Aslam', 'Usama']

print("Initial invitation messages:")
for guest in guests:
    print(f"Hello {guest}, you are invited to the party!")
total_guests : int = len(guests)
print(total_guests)



# Exercise 3.5....

guests = ['ali', 'Aslam', 'Usama']

print("Initial invitation messages:")
for guest in guests:
    print(f"Hello {guest}, you are invited to the party!")

absent = 'Aslam'
print(f"\n{absent} can't make it to the party.")

new_guest = 'danish'
guests[guests.index(absent)] = new_guest
print("\nUpdated invitation messages:")
for guest in guests:
    print(f"Hello {guest}, you are invited to the party!")

# Exercise 3.6....


names = ["danish", "ali", "aslam"]

print("Initial invitation messages:")
for guest in names:
    print(f"{guest}, you are invited to dinner tonight.")

print("\nGreat news! We found a bigger table, so we have more space.")

names.insert(0, "saad")  
names.insert(2, "mohammed")  
names.append("danial")  
print("\nUpdated invitation messages:")
for guest in names:
    print(f"{guest}, you are invited to dinner tonight.")

# Exercise 3.7....

names = ["saad", "danish", "ali", "mohammed", "aslam", "sijad"]

print("Initial invitation messages:")
for guest in names:
    print(f"{guest}, you are invited to dinner tonight.")

print("\nWe can now invite only two people to dinner.")

while len(names) > 2:
    removed_guest = names.pop()
    print(f"Sorry {removed_guest}, we can't invite you to dinner.")

print("\nThe following guests are still invited:")
for guest in names:
    print(f"{guest}, you are still invited to dinner tonight.")
print(len(names))
del names[:]

print("\nFinal list of guests:", names)

# Exercise 3.8....

places = ['faisalabad', 'Faisal mosque', 'Peshawar', 'badshahi mosque', 'lahore']

print("Original list:")
print(places)

print("\nAlphabetical order (using sorted()):")
print(sorted(places))

print("\nOriginal list after sorted():")
print(places)

print("\nReverse-alphabetical order (using sorted()):")
print(sorted(places, reverse=True))

print("\nOriginal list after sorted(reverse=True):")
print(places)

places.reverse()
print("\nList after reverse():")
print(places)

places.reverse()
print("\nList after reversing again to original order:")
print(places)

places.sort()
print("\nList after sort():")
print(places)

places.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(places)

# Exercise 3.9....---------------------------------------------------------------------
# i did this exersice in exercise 3.4 nad 3.7



# Exercise 3.10...--------------------------------------------------------------------
