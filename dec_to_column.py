char = "zabcdefghijklmnopqrstuvwxyz"
while True:
    a = int(input())
    b = ""
    while not a <= 26:
        b += char[a % 26]
        a //= 26
    else:
        b += char[a - 1]
    print(b[::-1])
