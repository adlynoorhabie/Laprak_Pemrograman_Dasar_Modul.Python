n, x = input().split()
n = int(n)
x = int(x)

total = 0
sum_of_totals = 0
expression = ("")
for i in range(1, n + 1):
    multiple = i * x
    total += multiple
    if i == 1:
        expression = (f"({i} * {x})")
    else:
        expression = (f"({i} * {x}) + " + expression)
    print(f"{expression} = {total}")
    
    sum_of_totals += total
print(sum_of_totals)