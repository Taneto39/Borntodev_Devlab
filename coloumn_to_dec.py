char_list = "abcdefghijklmnopqrstuvwxyz"
while True:
    a = input().lower()
    b = 0
    for idx, char in enumerate(reversed(a)):
        b += (char_list.index(char) + 1) * (26 ** idx)
    print(b)