import os

author = "Deart Ivan"

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def show_curr_dir():
    """
    Функция показывает текущую дерикторию
    """
    return print("Текущая дериктория: ", os.getcwd())


def list_dir():
    """
    Функция выводит нумерованный список папок текущей дериктории
    """
    print("Список папок в текущей директории: ")
    dir_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))
    for i, dir_name in enumerate(dir_list):
        print(i, dir_name)


def choose_dir(i):
    """
    Функция возвращает имя папки, выбранной пользователем из списка по номеру
    """
    dir_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))
    try:
        if int(i) in range(0, len(dir_list)):
            return dir_list[int(i)]
        else:
            print("Направильно набран номер")
            return ""
    except ValueError:
        return ""


def change_dir():
    """
    Функция делает выбор и переход в выбранную папку.
    Выбор возможен только из существующих папок
    """
    list_dir()
    new_choice = input("Выбeрите нужную папку для перехода: ")
    new_dir = choose_dir(new_choice)
    print("Вы выбрали папку: ", new_dir)
    if new_dir:
        curr_dir = os.getcwd()
        dir_path = os.path.join(curr_dir, new_dir)
        try:
            os.chdir(dir_path)
            print("Переход в папку {} состоялся".format(new_dir))
        except FileNotFoundError:
            print("Папка {} не существует".format(new_dir))
    else:
        print("Переход в папку не состоялся")
    show_curr_dir()


def show_all():
    """
    Функция выводит содержимое текущей директории
    """
    show_curr_dir()
    print("Содержимое текущей директории: ", os.listdir(os.getcwd()))


def del_dir():
    """
    :return: Функция удаляет выбранную папку
    """
    list_dir()
    new_choice = input("Выбeрите нужную папку для удаления: ")
    my_dir = choose_dir(new_choice)
    print("Вы выбрали папку: ", my_dir)
    if my_dir:
        curr_dir = os.getcwd()
        dir_path = os.path.join(curr_dir, my_dir)
        try:
            os.rmdir(dir_path)
            print("Папка {} удалена успешно".format(my_dir))
        except OSError:
            print("Папку {} не получается удалить".format(my_dir))
    else:
        print("Удаление не состоялось")


# создание новой папки, если таковой уже не существует
def create_dir():
    """
    Функция создаёт новую папку, если такой не существует
    """
    my_dir = input("Введите имя новой папки: ")
    if my_dir:
        curr_dir = os.getcwd()
        dir_path = os.path.join(curr_dir, my_dir)
        try:
            os.mkdir(dir_path)
            print("Папка {} успешно создана".format(my_dir))
        except FileExistsError:
            print("Папка {} уже существует".format(my_dir))
        return
    else:
        print("Создать папку не получилось")


titles = {"1": "Перейти в папку",
          "2": "Просмотреть содержимое текущей папки",
          "3": "Удалить папку",
          "4": "Создать папку"}
actions_numbers = "1234"
actions = {"1": change_dir,
           "2": show_all,
           "3": del_dir,
           "4": create_dir}
while True:
    print("ВЫБЕРИТЕ ОПЕРАЦИЮ ИЗ СПИСКА:")
    for key in actions_numbers:
        print(key, titles[key])
    print("q: Закончить работу с программой")
    key = input(" Ваш выбор: ")
    if key in actions_numbers:
        actions[key]()
    elif key == "q":
        print("Счастливо!")
        break
    else:
        print("Что-то не так \n")
