listX = []
listResult_Index = []
x = 0
y = 0

#สร้าง list พัสดุ
for i in range(int(input())):
    listX.append(input())

#สร้าง list index
findThis = input()
for i in listX:
    y += 1
    if findThis == i:
        listResult_Index.append(y)

#output
print("Position: ", end="")
for i in listResult_Index:
    x += 1
    print(i, end="")
    if x != len(listResult_Index):
        print(",", end="")
