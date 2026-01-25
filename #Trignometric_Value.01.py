import math
angle = float(input("Enter angle in degrees: "))

angle_rad = math.radians(angle)
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

print(f"\nFor angle = {angle}\u00B0: ")
print(f"sin = {sin_val:.3f}")
print(f"cos = {cos_val:.3f}")
print(f"tan = {tan_val:.3f}")