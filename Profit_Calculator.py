#Profit Calculator
actual_cost = int(input("Enter the actual amount: "))
sale_amount = int(input("Enter the sale amount: "))

if(sale_amount > actual_cost):
    profit= sale_amount-actual_cost
    print("Total profit is: ",profit)

else:
    print("No profit")