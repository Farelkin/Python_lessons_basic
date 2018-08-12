import random

author = "Deart Ivan"

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


NAME = ("А.", "Б.", "В.", "Г.", "Д.", "Е.", "М.", "Н.", "П.", "Р.")
SURNAME = ("Иванов", "Смирнов", "Петров","Сидоров","Сергеев", "Дмитриев", "Алексеев", 
           "Андреев", "Ильин", "Александров")
SUBJECT = ("Математика", "Русский язык", "Физика", "Литература", "Английский язык", "Химия", 
           "Информатика", "История", "География", "ИЗО")


class School:
    def __init__(self, name):
        self.name = name
        self.Classes = []
        
    def add_class(self, Class):
        self.Classes.append(Class)
        
    def show_classes(self):
        print("Школа " + self.name + " содержит: ")
        for i in self.Classes:
            print(i)
            
    def show_class(self, name):
        for i in self.Classes:
            if i.name == name:
                i.show_class()
                
    def show_pupil_info(self, name):
        for i in self.Classes:
            for j in i.Pupils:
                if j.name == name:
                    for k in i.Teachers:
                        print("Ученик " + j.name + ", класс " + i.name + ", учитель " + k.name + 
                                ", предмет " + k.subject)
                        
    def show_pupil_parents(self, name):
        for i in self.Classes:
            for j in i.Pupils:
                if j.name == name:
                    j.show_parents()
                    
    def rand_school(self, classes, pupils, subjects):
        for i in range(int(classes)):
            rclass = Class(str(random.randint(1,11))+random.choice(("А", "Б", "В", "Г")))
            self.add_class(rclass)
            for j in range(int(pupils)):
                rclass.add_pupil(Pupil(random.choice(SURNAME) + " " + random.choice(NAME) + random.choice(NAME),
                                       random.choice(SURNAME) + " " + random.choice(NAME) + random.choice(NAME),
                                       random.choice(SURNAME) + "а " + random.choice(NAME) + random.choice(NAME)))
            for k in range(int(subjects)):
                rclass.add_teacher(random.choice(SURNAME) + " " + random.choice(NAME) + 
                                   random.choice(NAME), random.choice(SUBJECT))
 
 
class Class:
    def __init__(self, name):
        self.name = name
        self.Pupils = []
        self.Teachers = []
        
    def add_pupil(self, pupil):
        self.Pupils.append(pupil)
        
    def add_teacher(self, name, subject):
        self.Teachers.append(Teacher(name, subject))
        
    def show_class(self):
        print("Класс " + self.name + " содержит: ")
        for i in self.Pupils:
            print(i.name)


class Pupil:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
        
    def show_parents(self):
        print("Отец: " + self.father)
        print("Мать: " + self.mother)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
