n = int(input())

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

print(f"{n}! = {faktorial(n)}")