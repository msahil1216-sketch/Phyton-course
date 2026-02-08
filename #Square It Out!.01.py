Start = int(input("Start number: "))
End = int(input("End number: "))

squares = [n**2 for n in range(Start, End+1)]
even = [s for s in squares if s % 2 == 0]
odd = [s for s in squares if s % 2 != 0 ]

print(f"\nSquares: {squares}")
print(f"Even: {even}")
print(f"Odd: {odd}")