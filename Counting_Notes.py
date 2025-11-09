#Total number as input
amount = int(input("Please enter the amount for withdraw"))

#Calculating the number of notes of different denominations
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("Number of notes of 100 rupees = ", note_1)
print("Number of notes of 50 rupees = ", note_2)
print("Number of notes of 10 rupees = ", note_3)