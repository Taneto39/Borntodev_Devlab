"""โดร่าและผองเพื่อนของเธอได้ทำการสำรวจเกาะต่างๆ จากแผนที่ของเธอ
ซึ่งเธอต้องการให้คุณช่วยนับเกาะในแผนที่ว่ามีจำนวนเกาะทั้งหมดกี่เกาะในแผนที่ ซึ่งในแผนที่นั้น จะใช้ #
แทนสัญลักษณ์ของพื้นดิน และ . แทนสัญลักษณ์ของน้ำ ซึ่งถ้าพื้นดินอยู่ติดกัน(ทิศเหนือ ทิศใต้
ทิศตะวันออกและทิศตะวันตก)จะถือว่าเป็นเกาะเดียวกัน """
scale_matrix = [int(i) for i in input().split(" ")]
matrix = []
around = []
result = 0
for _ in range(scale_matrix[0]):
    r = [char for char in input()]
    matrix.append(r)


def find_abs(a):  # สำหรับเกาะใหม่, ส่งกลับพิกัดที่มี"#"
    for row, v_row in enumerate(a):
        for column, ele in enumerate(v_row):
            if ele == "#":
                return [row, column]
    else:
        return False


def find_another(a):
    b = [[a[0] + 1, a[1]], [a[0], a[1] + 1],
         [a[0] - 1, a[1]], [a[0], a[1] - 1]]
    # ลบพิกัดไม่ถูกต้องออก
    c = b.copy()
    for r_c in b:
        if not (0 <= r_c[0] < scale_matrix[0] and 0 <= r_c[1] < scale_matrix[1]):  # เช็คพิกัดว่าอยู่ในสเกลหรือไม่
            c.remove(r_c)
    else:
        b = c.copy()
    # ลบพิกัดที่ไม่มี"#"ออก
    for r_c in b:
        if matrix[r_c[0]][r_c[1]] != "#":
            c.remove(r_c)
    else:
        b = c.copy()
    if b:
        for r_c in b:
            matrix[r_c[0]][r_c[1]] = "."
        return b
    else:
        return False


while find_abs(matrix):
    start_coordinates = find_abs(matrix)
    matrix[start_coordinates[0]][start_coordinates[1]] = "."
    around = find_another(start_coordinates)
    while around:
        for i in around:
            new = find_another(i)
            if new:
                for j in new:
                    around.append(j)
            around = [value for value in around if value != i]
    result += 1
print(result)
