x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

x = 0.5
if (type(x) is not float):
    print("true")
else:
    print("false")

x = 79
y = 79

if (x is y):
    print("x and y same identity")
else:
    print("x and y are different")

y = 60

if (x is not y):
    print("x and y are different")
else:
    print("x and y are same")