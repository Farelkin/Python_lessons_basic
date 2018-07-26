author = "Deart Ivan"
import math
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.

num = input("Введите целое произвольное число: ")
numList = list(num)
numList.sort()
print("Самая большая цифра числа: ", numList[-1])

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

a = int(input("Ведите два числа:\na = "))
b = int(input("b = "))

a = a + b
b = a - b
a = a - b

print("a = ", a, "b = ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Введите коэффициенты a, b, c квадратного уравнения ax2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print(" Дискриминант D = %.2f" % discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")