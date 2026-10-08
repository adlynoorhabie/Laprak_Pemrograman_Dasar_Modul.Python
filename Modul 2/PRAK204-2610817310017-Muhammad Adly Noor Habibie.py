radius, height = input().split()
radius = float(radius)
height = float(height)

phi = (22 / 7)

volume = (phi * radius**2 * height)
surface_area = (2 * phi * radius * (radius + height))
circumference = (2 * phi * radius)

print(f"Volume = {volume:.2f}")
print(f"Luas = {surface_area:.2f}")
print(f"Keliling = {circumference:.2f}")