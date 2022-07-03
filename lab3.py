import random
# 1 Введите список чисел с клавиатуры до тех пор, пока не
# введете 0 Удалите из списка каждый третий элемент
list1 = list()
while True:
    i = int(input())
    if i != 0:
        list1.append(i)
    else:
        break
print(list1)
del list1[2::3]
print(list1)

# 2 Поменять местами в списке две его половины. Например, из
# списка [1,2,3,4,5] получить список [3,4,5,1,2]
list2 = [int(i) for i in input().split()] 
print(list2)
x = len(list2) // 2
list2 = list2[x:] + list2[:x]   
print(list2)

# 3 Создать случайный список из десяти чисел от -2 до 2
# Заменить в нем все единицы на число 5
list3 = [random.randint(-2, 2) for i in range(10)]
print(list3)
list3 = list(map(lambda x: 5 if x == 1 else x, list3))
print(list3)

# 4 Создать случайный список из десяти чисел от -2 до 2 Удалить
# в нем все единицы.
list4 = [random.randint(-2, 2) for i in range(10)]
print(list4)
list4 = list(filter(lambda x: x != 1, list4))
print(list4)

# 5 Создать случайный список из двадцати чисел от -5 до 5
# Определить самый часто встречающийся элемент в нем
list5 = [random.randint(-5, 5) for i in range(20)]
print(list5)
max_count = 0
max_elem = None
for i in list5:
    if list5.count(i) > max_count:
        max_count = list5.count(i)
        max_elem = i
print("самый часто встречающийся элемент списка: ", max_elem)