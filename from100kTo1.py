x = input()

def sum_numeric(s_number):
    a = 0
    for i in s_number:
        a += int(i)
    return str(a)

while len(x) != 1:
    x = sum_numeric(x)
print(x)