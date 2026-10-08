Shoes_Price_A = (400000)
Shoes_Price_B = (350000) 

discout_13_percent = (Shoes_Price_A * 0.13)
Total_Price_A = (Shoes_Price_A - discout_13_percent)
discout_21_percent = (Shoes_Price_B * 0.21)
Total_Price_B = (Shoes_Price_B - discout_21_percent)

print("Harga sepatu A adalah ",Shoes_Price_A)
print("Harga sepatu B adalah ",Shoes_Price_B)
print(f"Sepatu A mendapat diskon 13% sehingga harganya menjadi {Total_Price_A:.0f}")
print(f"Sepatu B mendapat diskon 21% sehingga harganya menjadi {Total_Price_B:.0f}")