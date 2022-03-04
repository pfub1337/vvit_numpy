import numpy as np


def output(matrix, size):
    print('+-------' * (size + 1) + '+')
    print('|\t\t', end='')
    for x in range(size):
        print(f'|\t\033[32m{x + 1}\033[0m\t', end='')
    print('|\n' + '+-------' * (size + 1) + '+')
    for i in range(size):
        print(f'|\t\033[32m{i + 1}\033[0m\t|\t', end='')
        for j in range(size):
            print(int(matrix[i, j]), end='\t|\t')
        print('\n' + '+-------' * (size + 1) + '+\n', end='')


a = np.random.randint(-10, 10, (5, 5))

print("Матрица:")
output(a, 5)
print("Сумма третьего столбца и второй строки:", sum(a[:, 2]) + sum(a[1]), '\n')

a[[0, 2]] = a[[2, 0]]
print("Замена первой и третьей строки:")
output(a, 5)
print("Сумма первой и третьей строки:", sum(a[0]) + sum([2]), '\n')

a[1:4, 1:4] = np.zeros((3, 3))
print("Замена центральной области 3 х 3 на нули:")
output(a, 5)

block_size = int(input('\nРазмер одного блока: '))
block_count = int(input('Количество блоков: '))
zeros = np.zeros((block_size, block_size))
block_zeros = []
for i in range(block_count):
    block_str = []
    for j in range(block_count):
        block_str.append(zeros)
    block_zeros.append(block_str)
block_matrix = np.block(block_zeros)
for i in range(block_count):
    block_matrix[i * block_size: block_size + i * block_size, block_size * (block_count - i - 1):block_size * (block_count - i)] = np.random.randint(-10, 10, (block_size, block_size))

print('Блочная матрица:')
output(block_matrix, block_size * block_count)
