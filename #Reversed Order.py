#Reversing Digits

num = int(input("Please Enter your Number: "))

reversed_num = 0
temp = abs(num)

while temp > 0:
    last_digit = temp % 10
    reversed_num = reversed_num * 10 + last_digit
    temp = temp // 10

if num < 0:
    reversed_num = -reversed_num

print(f"Original Number: {num}")
print(f"Rversed Number: {reversed_num}")