# EXERCISE 5.1......

# if-else statement:
# Example 1
vacation_city: str = "Islamabad"

if vacation_city:
    print(vacation_city == "Islamabad")
    print(f"We're going to {vacation_city}")
    
if vacation_city:
    print(vacation_city == "Lahore")
    print(f"We're not going to {vacation_city}")
    
# Example 2
transport: str = "Faisal Movers"

if transport:
    print(f"\n{transport == 'Faisal Movers'}")
    print(f"We're going to {vacation_city} on {transport}")
    
if transport:
    print(f"{transport == 'Skyways'}")
    print(f"We're not going to {vacation_city} on {transport}")

# Example 3
cash: int = 2000

if cash:
    print(f"\n{cash == 2000}")
    print("We have {cash} in our pocket")

# Example 4
car: str = "BMW"

if car:
    print(f"\n{car == 'BMW'}")
    print(f"We're going to {vacation_city} with {car}")
    
if car:
    print(f"{car == 'Mercedes'}")
    print(f"We're not going to {vacation_city} with {car}")
    
# Example 5
friends : list[str] = ["ali", "aslam", "rehan"]
if friends:
    print(f"\n{friends == ['ali', 'aslam', 'rehan']}")
    print(f"We're going to {vacation_city} with {friends}")

if friends:
    print(f"{friends == ['usman', 'danish', 'rehan', 'saad']}")
    print(f"We're not going to {vacation_city} with {friends}")

# =================================================================================

# Exercise 5.2....

# Tests for equality and inequality with strings
a = "Hello"
b = "hello"

if a == b:
    print(f"{a} and {b} are equal")
else:
    print(f"{a} and {b} are not equal")

# Tests using the lower() method

if a.lower() == b.lower():
    print(f"{a} and {b} are equal")
else:
    print(f"{a} and {b} are not equal")


# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

val1 = 10
val2 = 10

if val1 == val2:
    print(f"{val1} and {val2} are equal")
else:
    print(f"{val1} and {val2} are not equal")

num1 = 10
num2 = 20

if num1 <= num2:
    print(f"{num1} is less than to {num2}")
else:
    print(f"{num1} is not less than to {num2}")
    
# Tests using the and keyword and the or keyword
v1 = 10
v2 = 20
v3 = 30

if v1 < v2 and v1 < v3:
    print(f"{v1} is the smallest number")
    
if v1 < v2 or v1 <= v2:
    print(f"{v1} is less than {v2}")

# Test whether an item is in a list
num_list = [10, 20, 30, 40, 50]

if v1 in num_list:
    print(f"{v1} is in the list")

if v1 in num_list and v2 in num_list and v3 in num_list:
    print(f"{v1}, {v2} and {v3} are in the list")

# Test whether an item is not in a list
num_list2 = [1, 2, 3, 4, 5]

if v1 not in num_list2:
    print(f"{v1} is not in the list")

if v1 not in num_list2 and v2 not in num_list2 and v3 not in num_list2:
    print(f"{v1}, {v2} and {v3} are not in the list")
    
# =========================================================================================

# EXERCISE 5.3....

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
else:
    print("No points earned.")
# ========================================================================================   
# EXERCISE 5.4....

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points for shooting the alien.")
    
# =========================================================================================

# EXERCISE 5.5....

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the alien.")
elif alien_color == 'red':
    print("Congratulations! You just earned 15 points for shooting the alien.")
else:
    print("Alien color not recognized. No points earned.")
    
# =========================================================================================

# EXERCISE 5.6....

