"""
Типы данных
"""

# #  Изменяемые типы данных:
# # list - список
# # set - множество
# # dict - словари
# """
# Неизменяемые типы данных:
# tuple - кортеж
# str - строки (string)
# bool - логический тип данных
# int - целые числа
# float - дробные числа
# complex - сложные числа
# frozenset - неизменяемое множество
# NoneType - тип данных, для обозначения пустого значения (None)
# """

"""
Переменные
"""

# a = 1

# # Название переменной не должно начинаться с цифр или спец символов
# # num = 10 OK
# # 1num = 10 ERROR - SyntaxError


# # Если название перменной сост из нескольких слов,
# # стоит разделять их нижним подчеркиванием(underscore).
# # Также, раделение сло не должно содержать спец символов и пробелов

# my_num = 33 # ok - snake_case
# myNum = 34 # ok - camelCase - js

# # Название переменных не должны совпадать с названиями ключевых слов (зарезервированных)

# # Регистр в питоне играет большую роль  
# a = 10
# A = 20
# # Разные переменные 

# # Переменные состоящие из символов верхнего регистра по общему соглашению, 
# # являются костантами (неизменяемые/постоянные)

# URL = 'google.com'

# # Хорошая практика; называть переменные так, чтобы было понятно, что они в себе хранят 
 
# # Литералы - символы, служащие для обозначения данных

# num = 10
# my_float = 3.5
# string = ''
# list_of_num = [1, 2, 3]
# tuple_of_num = (1, 2, 3)
# set_of_nums = {2, 7.7, ' '}
# dicttionary = {'word': 'слово'}
# none_type = None
# true = True
# false = False
"""
Многострочные комментраии
Чаще исплользуютя
для документации к коду
"""
# Однострочные комментарии используются для краткого описания строки 
"""
Функции print(), input(), type(), id()
"""
# print() - функция для вывода в терминал
# # input() - функция для ввода информации из терминала
# string = input()
# print(string)

# age = int(input('Введите возраст: '))
# print('Ваш возраст: ', age)

# Python - язык с динамической типизацией и строгой типизацией
# num = 22
# print(type(num))
# type - функция для вывода типа переданных данных
# id
a=10
b=10
print(id(a))
print(id(b))