#Taking marks as input from the User
print("Enter Marks obtained in 4 subjects: ")
Math = int(input("Math:"))
English = int(input("English:"))
Science = int(input("Science:"))
History = int(input("History:"))

#Calculate Percentage 
Sum = Math+English+Science+History
print("The Sum of all 4 subjects is: ", Sum)

Average = Sum/4
print("The Average of all 4 subjects is: ", Average)

Percentage = (Sum/400)*100
print("The Percentage is: ", Percentage)
