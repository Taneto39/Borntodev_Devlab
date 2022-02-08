matrix = []
for _ in range(3):
    matrix.append([int(i) for i in input().split(" ")])
matrix_name = input()
minor_dict = {'minor1': (matrix[1][1] * matrix[2][2]) - (matrix[2][1] * matrix[1][2]),
              'minor2': (matrix[1][0] * matrix[2][2]) - (matrix[2][0] * matrix[1][2]),
              'minor3': (matrix[1][0] * matrix[2][1]) - (matrix[2][0] * matrix[1][1])}
coFactor_dict = {'co_factor1': minor_dict['minor1'] * matrix[0][0],
                 'co_factor2': minor_dict['minor2'] * -matrix[0][1],
                 'co_factor3': minor_dict['minor3'] * matrix[0][2]}
for i in range(1, 4):
    minor = minor_dict[f'minor{i}']
    co_factor = coFactor_dict[f'co_factor{i}']
    print(f'Minar {i} : {minor} and Co-Factor {i} : {co_factor}')
print(f'Determinant |{matrix_name}| : {sum(coFactor_dict.values())}')
