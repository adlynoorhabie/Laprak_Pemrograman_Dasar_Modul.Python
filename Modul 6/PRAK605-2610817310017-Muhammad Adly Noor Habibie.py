n = int(input())

input()
A = [list(map(int, input().split())) for _ in range(n)]

input()
B = [list(map(int, input().split())) for _ in range(n)]

print("Matriks AXB")
for i in range(n):
    row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        row.append(str(total))
    print(" ".join(row))