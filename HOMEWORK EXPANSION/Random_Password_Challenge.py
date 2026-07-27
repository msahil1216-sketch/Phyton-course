import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits

characters = lower + upper + numbers

password = []

for i in range(10):
    password.append(random.choice(characters))

random.shuffle(password)

password = "".join(password)

print("Random Password:", password)