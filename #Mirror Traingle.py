#Take input
print("half Pyramid Pattern of Stars (*): ")
n = int(input("Enter your number of rows: "))

#Outer loop to handle number of rows
for i in range(n, 0, -1):
 #Inner loop to handle number of columns
    for j in range(i):
      #Display result
        print("*", end="")
    print()