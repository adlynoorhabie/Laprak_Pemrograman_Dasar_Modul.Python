number = int(input())

for i in range(1, number + 1, 2):
    print(i, end=" ")
print()

if number % 2 == 0:
    odd = number
else :
    odd = number - 1

for i in range (odd, 1, -2):
    print(i, end=" ")