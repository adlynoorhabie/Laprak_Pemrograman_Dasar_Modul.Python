while True:
    print("Pilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")

    choice = input("masukkan pilihan : ")

    if choice == "5":
        print("Terimakasih, telah menggunakan kalkulator Adly")
        break
    elif choice == "1":
        a = float(input("masukkan nilai pertama : "))
        b = float(input("masukkan nilai kedua : "))
        print(f"Hasil pilihan {a:.2f} dengan {b:.2f} adalah {a + b:.2f}")
        continue
    elif choice == "2":
        a = float(input("masukkan nilai pertama : "))
        b = float(input("masukkan nilai kedua : "))
        print(f"Hasil pilihan {a:.2f} dengan {b:.2f} adalah {a - b:.2f}")
        continue
    elif choice == "3":
        a = float(input("masukkan nilai pertama : "))
        b = float(input("masukkan nilai kedua : "))
        print(f"Hasil pilihan {a:.2f} dengan {b:.2f} adalah {a * b:.2f}")
        continue
    elif choice == "4":
        a = float(input("masukkan nilai pertama : "))
        b = float(input("masukkan nilai kedua : "))
        print(f"Hasil pilihan {a:.2f} dengan {b:.2f} adalah {a / b:.2f}")
        continue
    else:
        print("Input anda salah, silahkan coba lagi ")