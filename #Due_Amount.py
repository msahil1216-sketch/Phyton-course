def calculate_change(bill, paid):
    change = paid - bill
    return change

bill_amount = 100
amount_paid = 200

due_amount = calculate_change(bill_amount, amount_paid)
print(f"The shopkeeper should return: ${due_amount}")