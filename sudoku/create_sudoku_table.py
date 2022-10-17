txt = '7 0 0 0 0 9 0 0 0\n' \
      '0 0 0 0 0 5 0 0 8\n' \
      '0 0 1 7 8 0 3 0 0\n' \
      '1 0 0 4 6 0 0 0 9\n' \
      '0 0 3 0 0 0 0 2 0\n' \
      '0 0 0 0 0 7 0 0 0\n' \
      '4 0 0 8 1 0 0 0 6\n' \
      '0 0 0 0 5 0 0 0 0\n' \
      '0 6 0 0 0 0 9 0 0'
print(txt)
table = []
print('[', end='')
for row in txt.split('\n'):
    table.append('['+', '.join([char for char in row.split(' ')])+']')
print(',\n'.join(table)+']')

