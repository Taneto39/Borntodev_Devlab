def scale(all_no, max_s, min_s):
    return [(((i - min(all_no))/(max(all_no)-min(all_no))) * (max_s - min_s)) + min_s for i in all_no]


min_scale = 0
max_scale = 1
column, row = int(input()), int(input())
list_no = []
for _ in range(column*row):
    list_no.append(float(input()))
list_scale = scale(list_no, max_scale, min_scale)
matrix = []
for r in range(row):
    list_row = []
    for c in range(column):
        list_row.append(list_scale[(r*column)+c])
    matrix.append(list_row)
for list_row in matrix:
    print(' '.join([f'{i:.4f}' for i in list_row]))