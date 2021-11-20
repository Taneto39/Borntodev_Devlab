l, u, d, s = 0, 0, 0, 0
x = input()
for i in x:
    if i.islower():
        l += 1
    if i.isupper():
        u += 1
    if i.isdigit():
        d += 1
    if not (i.isdigit() and i.isalpha()):
        s += 1
if l >= 1 and u >= 1 and d >= 1 and s >= 1 and 3 <= len(x) <= 20:
    print("Valid")
else:
    print("Invalid")
