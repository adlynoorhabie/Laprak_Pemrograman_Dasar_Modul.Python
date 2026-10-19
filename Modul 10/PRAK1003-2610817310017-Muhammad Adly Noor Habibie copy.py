Input_variabel = int(input())

def digit_total(n):
    if n < 10:
        return n
    else:
        return (n % 10) + digit_total(n // 10)

result = digit_total(Input_variabel)

print(f"Total digit dari {Input_variabel} adalah {result}")