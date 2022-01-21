dictValue = dict(I=1,
                 V=5,
                 X=10,
                 L=50,
                 C=100,
                 D=500,
                 M=1000)
x = int(input())
if x >= 1000:
    print("M" * (x // 1000), end="")
    x %= 1000
if x // 100 == 9:
    print("CM", end="")
elif x // 100 >= 5:
    print("D", end="")
    x %= 500
    print("C" * (x // 100), end="")
elif x // 100 == 4:
    print("CD", end="")
else:
    print("C" * (x // 100), end="")
x %= 100
if x // 10 == 9:
    print("XC", end="")
elif x // 10 == 5:
    print("L", end="")
    x %= 50
    print("X" * (x // 10), end="")
elif x // 10 == 4:
    print("XL", end="")
else:
    print("X" * (x // 10), end="")
x %= 10
if x == 9:
    print("IX", end="")
elif x >= 5:
    print("V", end="")
    x -= 5
    print("I" * x, end="")
elif x == 4:
    print("IV", end="")
else:
    print("I" * x, end="")
