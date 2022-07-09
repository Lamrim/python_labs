def print_matrix_to_file(matrix, file_name):
    n = len(matrix)
    m = len(matrix[0])
    with open(file_name, 'w', encoding='UTF-8') as my_file:
        for i in range(n):
            for j in range(m):
                print(a[i][j], end=' ', file=my_file)
            print(file=my_file)
            
def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()

# 1 Даны два числа n и m. Создайте матрицу размером n на m и
# заполните ее символами "." и "*" в шахматном порядке. В
# левом верхнем углу должна стоять точка.
print('Введите размерность матрицы')
n, m = int(input()), int(input())
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0 :
            a[i][j] = '.'
        else:
            a[i][j] = '*'
print_matrix(a)

# 2 Посчитать в файле 1.txt (там может быть все что угодно)
# количество слов длины 5
import re
counter = 0
with open('1.txt', 'r', encoding='UTF-8') as my_file:
    file_data = my_file.read()
    words = re.split('[^\w\-]', file_data)
    for word in words:
        if len(word) == 5:
            counter += 1
print(counter)

# 3 Создать случайную матрицу размера m x n, обнулить все
# элементы выше главной диагонали, записать ее в файл
import random
print('Введите размерность матрицы')
n, m = int(input()), int(input())
a = [[random.randrange(1, 10)] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if j > i:
            a[i][j] = 0
print_matrix_to_file(a, 'task3.txt')


# 4 Пусть есть шахматная доска 8х8 и номера клеток a и b, где
# стоит ладья. Покажите симоволом *, где стоит ладья и
# символами ! - все возможные пути, куда она может пойти
n = 8
print('Введите координату клетки')
a, b = int(input()), int(input())
avaliable_indexes = [i for i in range(1, 9)]
if a not in avaliable_indexes or b not in avaliable_indexes:
    print('Неверная координата')
else:
    mtx = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            mtx[i][b - 1] = '!'
            mtx[a - 1][j] = '!'
    mtx[a - 1][b - 1] = '*'
    print_matrix(mtx)

    



    

