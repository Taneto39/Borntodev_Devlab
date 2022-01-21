import math

x = input()
listX = x.split(" ")
n, m, y = int(listX[0]), int(listX[1]), int(listX[2])
b = n/(m-1)+y
a = n + b
print(math.floor(a), math.floor(b))