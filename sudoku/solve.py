from sudoku_f import *

# sudoku_table = [[0, 0, 7, 4, 0, 1, 0, 2, 0],
#                 [8, 0, 0, 0, 0, 0, 0, 0, 7],
#                 [0, 0, 0, 0, 0, 3, 0, 0, 0],
#                 [0, 5, 0, 0, 0, 0, 6, 0, 0],
#                 [0, 0, 8, 2, 0, 7, 0, 1, 0],
#                 [0, 0, 0, 0, 9, 0, 0, 0, 0],
#                 [0, 0, 4, 0, 3, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 8, 0, 0, 9, 0],
#                 [6, 0, 0, 9, 0, 4, 1, 0, 0]]
# sudoku_table = [[0, 6, 0, 0, 0, 0, 3, 0, 0],
#                 [0, 7, 0, 0, 1, 0, 0, 0, 0],
#                 [3, 0, 1, 0, 0, 2, 0, 4, 0],
#                 [0, 1, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 4, 0, 0, 8],
#                 [9, 0, 5, 0, 2, 0, 7, 0, 0],
#                 [0, 0, 0, 9, 0, 0, 0, 7, 0],
#                 [2, 0, 3, 0, 5, 0, 9, 0, 0],
#                 [6, 0, 0, 0, 0, 0, 0, 0, 0]]
# sudoku_table = [[5, 6, 2, 0, 8, 9, 3, 0, 0],
#                 [0, 7, 0, 0, 1, 0, 0, 0, 0],
#                 [3, 0, 1, 0, 0, 2, 0, 4, 0],
#                 [0, 1, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 4, 0, 0, 8],
#                 [9, 0, 5, 0, 2, 0, 7, 0, 0],
#                 [0, 0, 0, 9, 0, 0, 0, 7, 0],
#                 [2, 0, 3, 0, 5, 0, 9, 0, 0],
#                 [6, 0, 0, 0, 0, 0, 0, 0, 0]]
sudoku_table = [[0, 0, 7, 8, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 5, 0, 0],
                [0, 8, 0, 0, 6, 0, 3, 0, 9],
                [0, 9, 0, 0, 0, 0, 0, 5, 0],
                [0, 0, 4, 0, 0, 3, 9, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 7, 0],
                [2, 0, 0, 0, 0, 4, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 7, 0, 0, 3, 0, 8, 0, 6]]
solve = sudoku_table.copy()
write_possible(solve)
try_history = []  # pos, index, len, table
possible_list = []
index = 0
compare = True
while True:
    solve_by_only_one_possible(solve)
    if is_sudoku_filled(solve):
        break
    solve_by_unique(solve)
    if is_sudoku_filled(solve):
        break
    print('solve1')
    show_sudoku(solve)
    if there_one_list(solve):
        continue
    if compare or is_sudoku_conflict(solve):
        if compare:
            print('Compare')
            show_sudoku(solve)
        if is_sudoku_conflict(solve):
            print('Conflict')
        if is_sudoku_conflict(solve):
            index = try_history[-1][1] + 1
            solve = convert_to_table(try_history[-1][-1])
            while index == try_history[-1][2]:
                del try_history[-1]
                index = try_history[-1][1] + 1
                solve = convert_to_table(try_history[-1][-1])
                if len(try_history) == 1:
                    break
        else:
            index = 0
        x, y = first_list(solve)
        if index == 0:
            try_history.append([(x, y), index, len(solve[x][y]), convert_to_string(solve)])
        else:
            solve = convert_to_table(try_history[-1][-1])
            try_history[-1][1] = index
        possible_list = solve[x][y]
        solve[x][y] = possible_list[index]
        remove_possible(x, y, solve)
        show_sudoku(solve)
    if is_sudoku_filled(solve):
        break
    print('solve2')
    show_sudoku(solve)
    show_try(try_history)
    globals()['compare'] = True
# show_try(try_history)
# show_sudoku(solve)
# solve_by_try(solve, try_history)
# show_try(try_history)
show_sudoku(solve)
