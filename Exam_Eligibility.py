#Exam eligibility

#Take input for the student that he can attend the exam or not 
medical_cause = input("Did you have a Medical cause Y or N: ")

#Take input of the attendence
Attendence = int(input("Enter the attendence of the student: "))

#Checking the user input predicting output accordingly

if medical_cause == 'Y': #Checking the condition 1
    print("You are allowed")
else:
    if Attendence >= 75: #Checking the condition 2 
        print("You are allowed")
    else:
        print("You are not allowed")