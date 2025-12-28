num = float(input("Enter your decimal number: "))
whole = int(num)
fraction = num - whole

#Convert whole part
binary = ""
if whole == 0:
    binary = "0"
else:
    temp = whole
    while temp > 0:
        binary = str(temp % 2) + binary
        temp = temp // 2

#Convert fraction part
if fraction > 0:
    binary += "."
    temp = fraction
    for i in range(8):
        temp *= 2
        binary += "1" if temp >= 1 else "0"
        if temp >= 1:
            temp -= 1

print (f"Binary: {binary}")