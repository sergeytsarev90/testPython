# Транспонирование матрицы
matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

# Транспонирование
matrix_t = list(zip(*matrix))

# Вывод матриц
#print(matrix)
# print(matrix_t)

for item in matrix:
    print(item)

    # for i in item:
    #    print(i)
    # print(sum(item))
print('*'*25)

for item in matrix_t:
    print(list(item))

