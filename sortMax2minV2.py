listNumber = []
x = int(input())
for i in range(x):
    listNumber.append(int(input()))
listNumber.sort(reverse=True)
for i in listNumber:
    print(i)