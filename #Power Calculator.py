#Power Calculator

Number = int(input("Please Enter a Number: "))
n = int(input("Enter the value of the Power: "))

print(f"\n The Power of {Number}: ")

for i in range(1,n + 1):
    Result = Number ** i
    print(f"{Number}^{i} = {Result}")