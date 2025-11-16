#Checking Alphabets

Character = input("Enter your Character: ")

if (Character >= 'A' and Character <= 'Z') or (Character >= 'a' and Character <= 'z'):
    print(Character, "is an Alphabet")

else:
    print(Character, "is not an Alphabet")