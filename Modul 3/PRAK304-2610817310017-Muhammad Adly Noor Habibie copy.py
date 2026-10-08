N = int(input())

if N > 99:
    print("Anda Menginput Melebihi Limit Bilangan")
elif N == 0:
    print("Nol")
elif N < 10:
    print("Satuan")
elif N < 20:
    print("Belasan")
else:
    print("Puluhan")