import os
import time
import shutil

author = "Deart Ivan"

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir():
    """
    Функция создаёт девять директорий
    """
    a = 1
    while a <= 9:
        b = os.path.join(os.getcwd(), "dir_{}".format(a))  # Проверяем путь к директории
        try:
            os.mkdir(b)  # Создаём папку в директории
            print("dir_{}, создана!".format(a))
        except FileExistsError:
            print("Такой файл уже существует!")
        a += 1


def remove_dir():
    """
    Функция удаляет созданные девять директорий
    """
    a = 1
    while a <= 9:
        b = os.path.join(os.getcwd(), "dir_{}".format(a))  # Проверяем путь к директории
        try:
            os.rmdir(b)  # Удаляем папку в директории
            print("dir_{}, удалена!".format(a))
        except FileExistsError:
            print("Такого файла нет в этой директории!")
        a += 1


create_dir()
time.sleep(10)  # Пауза на 10 сек для того, что бы удостовериться, что директории созданы.
remove_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    return print(list(filter(lambda x: os.path.isdir(x), os.listdir())))


list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_files():
    return shutil.copy(r"Hw5Easy_Deart.py", r"Hw5Easy_Deart_copy.py")


copy_files()
