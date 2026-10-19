n = int(input())

def hanoi_step(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi_step(n - 1) + 1

print(f"Jumlah langkah minimum untuk {n}  cakram adalah {hanoi_step(n)}")