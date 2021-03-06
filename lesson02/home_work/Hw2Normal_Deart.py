import math
import random

author = "Deart Ivan"

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

numbers = [2, -5, 8, 9, -25, 25, 4]
trueNumbers = []
for i in numbers:
    if i < 0:
        i += 1
    elif math.sqrt(i).is_integer():
            trueNumbers.append(int(math.sqrt(i)))
    else:
        i += 1
print(trueNumbers)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input('Введите дату в формате dd.mm.yyyy: ')
d = int(date[:2])
m = int(date[3:5])
y = int(date[6:])
days = ['первое','второе','третье','четвертое','пятое','шестое','седьмое','восьмое','девятое','десятое','одиннадцатое',
         'двенадцатое','тринадцатое','четырнадцатое','пятнадцатое','шестнадцатое','семнадцатое','восемнадцатое',
        'девятнадцатое','двадцатое','двадцать первое','двадцать второе','двадцать третье','двадцать четвертое',
        'двадцать пятое','двадцать шестое','двадцать седьмое','двадцать восьмое','двадцать девятое','тридцатое',
        'тридцать первое']
months = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
print(days[d - 1], months[m - 1], y, 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n = int(input('Введите длину списка n: '))
a = []
for i in range(n):
    a.append(random.randint(-100, 100))
print(a)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2, 10]
def remove(lst):
    """Функция к задаче 4"""
    print('Исходный список: ', lst)
    lst2 = []
    for i in range(len(lst)):
        if not lst[i] in lst[:i]+lst[i+1:]:
            lst2.append(lst[i])
    print('Неповторяющиеся элементы исходного списка: ', lst2)
    lst2 = []
    for i in range(len(lst)):
        if not lst[i] in lst[:i]:
            lst2.append(lst[i])
    lst2 = list(set(lst))
    print('Элементы исходного списка, которые не имеют повторений: ', lst2)
remove(lst)
