a, b, i, j, x, y = input().split()
a = float(a)
b = float(b)
i = float(i)
j = float(j)
x = float(x)
y = float(y)

result = ((a - b) * i / j - x - y)

print(f"{result:.3f}")