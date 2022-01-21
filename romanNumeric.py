dictValue = dict(I=1,
                 V=5,
                 X=10,
                 L=50,
                 C=100,
                 D=500,
                 M=1000)
x = input()
y = dictValue.get(x[0])
for i in range(len(x)-1):
    if dictValue.get(x[i]) >= dictValue.get(x[i+1]):
        y += dictValue.get(x[i+1])
    else:
        y += dictValue.get(x[i+1])
        y -= dictValue.get(x[i])*2
print(y)