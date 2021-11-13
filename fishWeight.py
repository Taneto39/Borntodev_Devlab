def input_weight():
    return int(input("ใส่น้ำหนักปลา(กก.) ใส่'0'เมื่อปลาหมดแล้ว"))


x = input_weight()
listWeightFish = []

while x != 0:
    listWeightFish.append(x)
    x = input_weight()
minMax = input("ต้องการให้เรียงแบบไหน min=จากน้อยไปมาก max=จากมากไปน้อย").lower()
if minMax == "min":
    listWeightFish.sort()
else:
    listWeightFish.sort(reverse=True)

for i in listWeightFish:
    print(i, end=" ")
