x = int(input())
y = 2*x-1
for i in range(x):
    print(("*"*(((i+1)*2)-1)).center(y, " "))
x = list(range(x-1))
x.reverse()
for i in x:
    print(("*"*(((i+1)*2)-1)).center(y, " "))