x = input()
y = ""
z = 0
listX = []

for i in x:
    if i.isdigit():
        y += i
    else:
        if y != "":
            listX.append(y)
            y = ""
if y != "":
    listX.append(y)
for i in listX:
    z += int(i)
print(str(z).rjust(4, "0"))
