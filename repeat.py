# ให้ทำการสร้างพีระมิดจากข้อความที่ได้รับเข้ามาตามตัวอย่าง

# input
x = input()
listString = []

# create list
for i in x:
    listString.append(i)

# create reverse list
listReverse = listString.copy()
listReverse.pop(0)
listReverse = listReverse[::-1]

# create string and print
for i in range(len(x)):
    s = listReverse[len(listReverse)-i:len(listReverse)].copy()
    for j in range(i+1):
        s.append(listString[j])
    print((" ".join([str(elem) for elem in s])).center(len(x)*4-3, " "))
