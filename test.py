str_col_no = 141
char = "abcdefghijklmnopqrstuvwxyz"
plus_num = (4, 11)
r_num = 1
pre_col = str_col_no
txt = ""
while pre_col < 303:
    b = ""
    col_no = pre_col
    while not col_no <= 26:
        b += char[(col_no % 26) - 1]
        col_no //= 26
    else:
        b += char[col_no - 1]
    txt += b[::-1]
    if r_num == 1:
        pre_col += plus_num[r_num]
        txt += ":"
        r_num = 0
    else:
        pre_col += plus_num[r_num]
        print(txt)
        r_num = 1
        txt = ""
