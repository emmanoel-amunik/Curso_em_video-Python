def area(a, b):
    c = a * b
    print(f"The area of a {a} x {b} land is {c}m².")


print("    LAND CONTROL")
print("-" * 20)

land_width = float(input("Width (m): "))
land_length = float(input("Length (m): "))
area(land_width, land_length)
