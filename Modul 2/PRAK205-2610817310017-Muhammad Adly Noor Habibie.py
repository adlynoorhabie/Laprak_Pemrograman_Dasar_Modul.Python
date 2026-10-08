A, B = input().split()
A = float(A)
B = float(B)

base = ((B**2 - A**2) ** 0.5)
height = (A)
perimeter = (height + B + base)
area = ((base * height) / 2)

print(f"Alas = {base:g} cm")
print(f"Tinggi = {height:g} cm")
print(f"Keliling = {perimeter:g} cm")
print(f"Luas = {area:g} cm^2")