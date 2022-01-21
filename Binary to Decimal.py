a = input()[::-1]
result, y = 0, 0

for i in a:
    if i == "1":
        result += 2 ** y
    y += 1
print(result)
