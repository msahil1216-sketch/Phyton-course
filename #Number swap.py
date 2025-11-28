#Number Swapping

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

print(f"Before swapping: a = {a}, b = {b}, c = {c}")

Temporary_value = a 
a = b
b = c
c = Temporary_value

print(f"After swapping: a = {a}, b = {b}, c = {c}")