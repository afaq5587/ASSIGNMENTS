# EXERCISE 4.1....
favorite_pizzas : list[str] = ["spiccy", "crispy" , "crunchy"]
for pizza in favorite_pizzas:
    print(pizza)
    
    print(f"i like to eat {pizza} pizza!.")
    
# -------==========================================================

# EXERCISE 4.2......
animals : list[str] = ["dog", "cat", "goat"]
for animal in animals:
    print(animal)
    print(f"\n{animal}: would make a great pet")
    
print("\nAny of these animals would make a great pet!.")

# EXERCISE 4.3.......

for i in range(1, 21):
    print(i)
    
# EXERCISE 4.4.......

# for l in range(1 , 10000000):
#     print(l)

# # EXERCISE 4.5.......




# EXERCISE 4.6.......
# odd numbers

for i in range(1, 21, 2):
    print(i)
    

# EXERCISE 4.7.......

# multiple of 3
multiple : list = []
for value in range(3 , 31):
    multiple.append(value*3)
    
print(multiple)

# EXERCISE 4.8.......

# CUBES

cubes : list = []
for cube in range(1 , 10):
   cubes.append(cube**3)
    
print(cubes)

# EXERCISE 4.9.......
# list comprehensive
l_cube : list = [n**3 for n in range(1, 11)]
print(l_cube)

# EXERCISE 4.10.......
# slicing
numbers : list[int] = [9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54,]      
print(f"first three sliced numbers are :  {numbers[:3]}" )
print(f"the middle sliced numbers are : {numbers[8:11]}")
print(f"the last three sliced numbers are : {numbers[13:]}")


# EXERCISE 4.11.......
my_pizzas : list[str] = ["spiccy", "crispy" , "crunchy"]

friend_pizzas : list[str] = ["spiccy", "crispy" , "crunchy"]

my_pizzas.append("large sized")
friend_pizzas.append("small size")
print(f"my pizzas are : {my_pizzas}")
print(f"my friend pizzas are : {friend_pizzas}")

# EXERCISE 4.12.......





# EXERCISE 4.13.......

# using tuples

foods : tuple[str,...] = ("biryani", "daal", "beef", "meat", "chanay")
for food in foods:
    print(food)
# adding in tuple
# foods.append("daal chawal")
# print(foods)

# resturant chage its menu
new_foods : tuple[str, ...] = ("biryani", "daal", "beef", "meat", "daal chawal")
print("All new foods that changed by owner are:")
for revisedfood in new_foods:
    print(revisedfood)


# EXERCISE 4.14.......

