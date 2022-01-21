a = int(input())
b = ""
while a != 0 and a != 1:
    b += str(a % 2)
    a = a//2
else:
    b += str(a)
print(int(b[::-1]))
