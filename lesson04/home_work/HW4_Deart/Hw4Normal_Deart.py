import re
import random
import os

author = "Deart Ivan"

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


def with_re_first_Ex(line):
       """
       Первый способ. С помощью регулярных выражений (Задание 1)
       """
       return print(re.findall('[a-z]+', line))


def without_re_first_Ex(line):
       """
       Второй способ. Без использования регулярных выражений (Задание 1)
       """
       line2 = "abcdefghijklmnopqrstuvwxyz"
       line3 = line[:]
       line4 = ""
       list = []
       k = 0
       i = 0
       while len(line3) > 0:
              while i < len(line3) and line3[i] in line2:
                     k += 1
                     i += 1
              if k > 1:
                     for j in range(k):
                            line4 += line3[j]
                     list.append(line4)
                     line4 = ""
                     k = 0
                     line3 = line3[i:]
                     i = 0
              elif k == 1:
                     list.append(line3[0])
                     k = 0
                     line3 = line3[1:]
                     i = 0
              else:
                     line3 = line3[1:]
       return print(list)


with_re_first_Ex(line)
without_re_first_Ex(line)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


def with_re_sec_Ex(line2):
       """
       Первый способ. С помощью регулярных выражений (Задание 2)
       """
       return print(re.findall("[a-z]{2}([A-Z]+)[A-Z]{2}", line2))

def without_re_sec_Ex(line_main):
       """
       Второй способ. Без использования регулярных выражений (Задание 2)
       """
       line_sub1 = "abcdefghijklmnopqrstuvwxyz"
       line_sub2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       line_sub3 = ""
       list = []
       b = 0
       while len(line_main) > 4:
              if line_main[2] in line_sub2 and line_main[1] in line_sub1 and line_main[0] in line_sub1 \
                      and line_main[3] in line_sub2 and line_main[4] in line_sub2:
                     line_main = line_main[2:]
                     while line_main[b] in line_sub2:
                            line_sub3 += line_main[b]
                            b += 1
                     line_sub3 = line_sub3[:-2]
                     list.append(line_sub3)
                     line_sub3 = ""
                     line_main = line_main[b:]
                     b = 0
              else:
                     line_main = line_main[1:]
       return print(list)


with_re_sec_Ex(line_2)
without_re_sec_Ex(line_2)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

def ex3():
    """
    Функция создает файл с 2500-значным числом и выводит самую длинную последовательность
    """
    name = "2500-digits number"
    new_path = os.path.join(name)
    file = open(new_path, 'w')
    for i in range(0, 2500):
        file.write(str(random.randint(0, 10)))
    file.close()

    file = open(new_path, 'r')
    pattern = "1{2,2500}|2{2,2500}|3{2,2500}|4{2,2500}|5{2,2500}|6{2,2500}|7{2,2500}|8{2,2500}|9{2,2500}|0{2,2500}"
    result = re.findall(pattern, file.readline())
    file.close()

    max = 0
    length = ""
    for j in result:
        if len(j) > max:
            length = j[:]
            max = len(j)
    print(length)


ex3()
