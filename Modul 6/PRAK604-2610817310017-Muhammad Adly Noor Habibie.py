code = input()
massage = input()

if len(code) != len(massage):
    print("Panjang kalimat berbeda, pesan palsu")
else:
    result = ""
    star = 0
    hashtag = 0
    
    for i in range(len(code)):
        k = code[i]
        p = massage[i]
        if k == " " and p == " ":
            result += " "
            continue

        if k == p:
            result += "*"
            star += 1
        else:
            result += "#"
            hashtag += 1

    print(result)
    print("* =", star)
    print("# =", hashtag)

    if star >= hashtag:
        print("Pesan Asli")
    else:
        print("Pesan Palsu")