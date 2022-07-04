# • В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0, если x = 0
# Напишите эту функцию
def sign(x):
    if x > 0: 
        return 1
    elif x < 0:
        return -1
    else: 
        return 0

print(sign(0))

# Вводятся натуральные числа A и B. (A<B). Функция печатает через
# пробел все простые на отрезке [A,B].
def prime_numbers(a, b):
    result = []
    if a > b:
        a, b = b, a
    for num in range(a, b + 1):
        if num > 1 and all(num % i != 0 for i in range(2, num)):
            result.append(num)
    print(*result)

A = int(input("Введите натуральное число А:"))
B = int(input("Введите натуральное число B:"))
prime_numbers(A, B)

# Написать функцию, в которую передается число N. В ней необходимо
# ввести N чисел. Вернуть надо минимум и максимум
# последовательности.
def input_chain(n):
    chain = []
    for i in range(n):
        print("Введиите число ", i + 1)
        chain.append(float(input()))
    min_num = min(chain)
    max_num = max(chain)
    return min_num, max_num
        
N = int(input("Введите N:"))
min_num, max_num = input_chain(N)
print("Минимум = ", min_num, ", максимум =", max_num)

# Напишите программу, которая запрашивает ввод двух значений. Если
# хотя бы одно из них не является числом, то должна выполняться
# склейка строк. В остальных случаях введенные числа суммируются.
value1 = input("Введите первое значение:")
value2 = input("Введите второе значение:")

try:
    print("Сумма чисел =", float(value1) + float(value2))
except:
    print(value1 + value2)