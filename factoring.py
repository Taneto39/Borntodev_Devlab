# code V1
"""
x = int(input())

# make prime list
pList = [2, 3]
for i in range(4, x+1):
    for j in pList:
        if i % j == 0:
            break
    else:
        pList.append(i)

# factoring & print
while x not in pList:
    for i in pList:
        if x % i == 0:
            print(i)
            x /= i
            break
print(int(x))
"""

# code V2
# It's faster than V1
x = int(input())
y = 2

# factoring & print
while x != 1:
    for i in range(2, int(x)+1):
        if x % i == 0:
            print(i)
            x /= i
            break
    y += 1
