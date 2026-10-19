n = int(input())

if n == 0:
    print(0)
else:
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(str(a))
        a, b = b, a + b
    print(" ".join(fib))