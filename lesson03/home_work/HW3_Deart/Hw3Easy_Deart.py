author = "Deart Ivan"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    if ndigits > 0:
        number1 = str(number)
        dot = number1.find(".")
        number2 = number1[:dot]
        number3 = number1[dot+1:]
        if int(number3[ndigits]) >= 5:
            number3 = str(int(number3[:ndigits])+1)
            if len(number3) != len(number3[:ndigits]):
                l = len(number3)-1
            else:
                l = len(number3)
        else:
            number3 = number3[:ndigits]
            l = len(number3)
        number = int(number2) + int(number3)/(10**l)
    else:
        number1 = str(number)
        dot = number1.find(".")
        number2 = number1[:dot]
        number3 = number1[dot+1:]
        if int(number3[ndigits]) >= 5:
            number = int(number2)+1
        else:
            number = int(number2)
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    list = []
    sum1 = 0
    sum2 = 0
    while ticket_number > 0:
        list.append(ticket_number % 10)
        ticket_number //= 10
    for i in range(3):
        sum1 += list[i]
        sum2 += list[i + 3]
    if sum1 == sum2:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(123214))
print(lucky_ticket(436751))
