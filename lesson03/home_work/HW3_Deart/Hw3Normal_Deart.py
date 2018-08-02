author = "Deart Ivan"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    """
    Функция возвращает ряд Фибоначчи с n-элемента до m-элемента
    :param n: от
    :param m: до
    :return: ряд
    """
    def fib(f):
        """
        Функция возвращает число Фибоначчи
        :param f: порядковый номер числа Фибоначчи в ряду
        :return: число Фиббоначи
        """
        if f < 3:
            return 1
        return fib(f - 1) + fib(f - 2)
    line = []
    i = n
    while i <= m:
        line.append(fib(i))
        i += 1
    return line


print(fibonacci(5, 10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    Алгоритм сортировки выбором
    """
    a = origin_list
    for i in range(len(a)):
        idxMin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter1(arg, list):
    list1 = []
    for i in list:
        if i != arg:
            list1.append(i)
    print(list1)


filter1(1, [1, 2, 3, 4, 1, 1, 5, 6, 7, 1, 8, 9, 1, 1])

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def length(x1, x2, y1, y2):
    """
    Функция выводит длину ветора
    """
    l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    return l


def slope(x1, x2, y1, y2):
    """
    Функция вычисляет наклон вектора
    """
    s = (y1 - y2) / (x1 - x2)
    return s


x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
x3 = int(input("Введите x3: "))
y3 = int(input("Введите y3: "))
x4 = int(input("Введите x4: "))
y4 = int(input("Введите y4: "))
# проверяем равность длин и наклон векторов
if length(x1, x2, y1, y2) == length(x3, x4, y3, y4) and slope(x1, x2, y1, y2) == slope(x3, x4, y3, y4):
    print("Да")
else:
    print("Нет")
