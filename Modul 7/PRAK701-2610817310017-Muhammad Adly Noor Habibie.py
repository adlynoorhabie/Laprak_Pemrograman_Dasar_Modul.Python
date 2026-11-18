first_name = input("Nama Depan: ")
last_name = input("Nama Belakang: ")
full_name = first_name + " " + last_name

print("Nama lengkap:", full_name)
print("Panjang nama (tanpa spasi):", len(full_name.replace(" ", "")))