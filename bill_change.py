"""โปรแกรมการทอนเงินให้กับลูกค้า
เพื่อแก้ปัญหาการไม่มีทอนหรือเงินขาดมเงินเกิน
ตามแคชเชียร์ ที่ร้านสะดวกซื้อ โดยการ จำแนก
ประเภทของธนบัตรในแคชเชียร์และ นับจำนวนของธนบัตรประเภทนั้นๆ
จากนั้นให้โปรแกรมทำการคำนวนเงินทอนและ เลือกประเภทของธนบัตรที่ต้องทอน
เพื่อป้องกัน การทอนธนบัตรผิดชนิด และ เพื่อให้ง่ายต่อการตรวจสอบว่าในแคชเชียร์ในมีธนบัตรแต่ละประเภทเพียงพอที่จะบริการลูกค้าหรือไม่
"""
total_change = -int(input())+int(input())
bill_available = []

print("change:", total_change)
txt = "cash: {} amount: {}"
for _ in range(6):
    bill_available.append([int(i) for i in input().split()])
for i in bill_available[1:]:
    bill_value = 0
    if total_change >= i[0]:
        bill_value = total_change // i[0] if i[0] * i[1] >= total_change else i[1]
        print(txt.format(i[0], bill_value))
        total_change -= i[0] * bill_value
