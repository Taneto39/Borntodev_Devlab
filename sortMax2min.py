listNumber = []
for i in range(5):
    listNumber.append(int(input()))
listNumber.sort(reverse=True)
for i in listNumber:
    print(i)