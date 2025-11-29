print("Select your ride: ")
print("1. Bike")
print("2. Car")

Choice = int(input("Enter your choice: "))

if(Choice == 1):
    print("what type of bike? ")
    print("1. Scooty\n")
    print("2. scooter\n")

    Choice2 = int(input("Enter your Choice2: "))
    if Choice2 == 1:
       print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif( Choice == 2 ): 
    print(" What type of Car? ")
    print("1. Sedan")
    print("2. XUV")
    Choice3 = int(input("Enter your Choice3: "))
    if Choice3 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong Choice!")