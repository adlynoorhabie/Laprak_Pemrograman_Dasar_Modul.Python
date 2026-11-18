n1, n2 = map(int, input().split())

if n1 != n2:
    print("jumlah tidak sama")
else:
    rows = [list(map(int, input().split())) for _ in range(2)]
    for j in range(n1):
        print(rows[0][j] * rows[1][j], end=" ")
    print()