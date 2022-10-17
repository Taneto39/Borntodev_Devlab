import math


def show_table(m):
    for r in m:
        print(' '.join([f'{i:03}' for i in r]))


length = math.sqrt(int(input()))
each_walk = [i//2 for i in range(2, length*2+1)][::-1]
matrix = []
for row in range(length):
    matrix.append([0 for _ in range(length)])
current_num = 1
x, y = -1, 0
down, right, up, left = 0, 0, 0, 0
for direction, step in enumerate(each_walk):
    if direction % 4 == 0:
        for _ in range(step):
            x += 1
            matrix[x][y] = current_num
            current_num += 1
        down += 1
        continue
    if direction % 4 == 1:
        for _ in range(step):
            y += 1
            matrix[x][y] = current_num
            current_num += 1
        right += 1
        continue
    if direction % 4 == 2:
        for _ in range(step):
            x -= 1
            matrix[x][y] = current_num
            current_num += 1
        up += 1
        continue
    if direction % 4 == 3:
        for _ in range(step):
            y -= 1
            matrix[x][y] = current_num
            current_num += 1
        left += 1
        continue
show_table(matrix)
print(f'UP : {up}')
print(f'DOWN : {down}')
print(f'LEFT : {left}')
print(f'RIGHT : {right}')