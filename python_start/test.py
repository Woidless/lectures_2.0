# name_of_list = ['Hello! Have a good day']
# new_list = [] 
# for i in name_of_list[0][len(name_of_list[0])//2:]:
#     new_list.append(i)
    
# for i in name_of_list[0][:(len(name_of_list[0]))//2]:
#     new_list.append(i)
 
# print(new_list)


# list_ = ['world', 'hello']
# new_list=[]
# for i in list_[::-1]:
#     new_list.append(i)
# print(new_list)

# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# print(suitcase)
# suitcase.pop()
# print(suitcase)
# suitcase.insert(0, 'панама')
# print(suitcase)


# list_ = []
# for i in range(0,101,2):
#     list_.append(i)
# print(list_)


# a = input()
# list_ = a.split(',')
# print(sorted(list_))

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# list_ = []
# for key, val in a.items():
#     if val == None:
#         a.pop(key)
# print(a)

# a1 = {1: 3}
# a2 = dict(gg = '5')
# a3 = dict.fromkeys(['c', 'g'])

# res = 1
# res *= 3
# print(res)

# list('makers')
# string = list("hello")
# dict_ = dict.fromkeys(string, 1)
# dict_['t'] = 2
# print(dict_)
# string = "pythonist"
# dict_ = {}
# for i in string:
#     dict_[i]
# dict_['t'] = 2
# print(dict_)

# string = "pythonist"
# string1 =list(string)
# i = 0
# dict_ = dict.fromkeys(string1, 1)
# for key in dict_:
#     i += 1
#     if i == 3:
#         dict_[key] = 2

# print(dict_)    

# Написать программу, которая будет запрашивать кол-во денег,
# к-ое вы хотите потратить. Если указанное число больше,
# чем денег в кошельке - программа предупреждает об этом и останавливается. 
# Иначе отнивает указанное число из кошелька о печатает кол-во оставшихся денег
# Если деньги заканчиваются - программа останавливается

# mon = 1000
# print(f'У вас осталось {mon}$')

# while mon > 0:

#     summa = input('Введите сумму, к-ю хотите снять ')
#     if not summa.isdigit():
#         print('Пожалуйста, введите целые числа ')
#         continue
#     else:
#         summa = int(summa)
        
#     if summa > mon:
#         print('Недостаточно средств ')
#         break
#     else:
#         mon -= summa
#     print(f'У вас осталось {mon}$')

# print('Работа завершена')
''' Кратное написание '''
# # loop
# my_list = []
# for i in range(50):
#     my_list.append(i)
# print(my_list)

# # list comprehension
# my_list2 = [i for i in range(50)]
# print(my_list2)
# #######
# # loop
# my_list3 = []
# for i in range(50):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list3)
'''  '''
# # list comprehension
# my_list4 = [i for i in range(50) if i % 2 == 0]
# print(my_list4)
'''  '''
# dictionary comprehension
# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# my_dict = {val: key for key, val in my_dict.items()}
# print(my_dict)
'''  '''
# list_ = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
# print(list_)

# n = int(input())
# dict_ = {i:i**2 for i in range(1, 501) if i % n == 0}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: [val for val in range(1, val + 1)]  for k, val in a.items()}
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {key: 'odd' if val % 2 == 1 else 'even' for key, val in dict_.items()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_.split() if i.isdigit()]
# print(list_)

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }

# new_dict = {key1: [key2 for key2 in val1.keys() if val1[key2] == max(val1.values())][0] for key1, val1 in dict_.items()}

# new_dict = {key1: [key2 for key2 in val.keys() if val[key2] == max(val.values())][0] for key1, val in dict_.items()}
# print(new_dict)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key: [val2 for val2 in val.values()][0] for key, val in my_dict.items()}
# print(dict_)

# dict_ = {2: 'string1', 1: 'str', 5: 'string112', 4: 'string12222'}
# dict_ = {key: len(val) if key % 2 == 0 else len(val)**3 for key, val in dict_.items()}
# print(dict_)

# fullset = set()
# for i in set1:
#     fullset.add(i)
# for i in set2:
#     fullset.add(i)

# set1 = {i for i in range(10)}
# set2 = {i for i in range(8, 18)}
# full_set = (set1 | set2)
# if len(full_set) == 20:
#     print('Ваш объединенный сет полностью уникальный!')
# else:
#     print(f'В этом сете было {(len(set1)+len(set2))-len(full_set)} повторения, его длина составляет {len(full_set)}')

# print(set1)
# print(set2)
# print(full_set)

''' def '''
# def foo():
#   var = 'переменная foo'
#   print('переменная в foo: ', var)                
  
#   def bar():
#     global var
#     var = 'переменная bar'
 
#   bar()

# foo()
# print('переменная в foo: ', var)
''' --- '''
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу измениться'
# my_func()
# print(x)
''' --- '''
# num = 3 

# def mul():
#   global num
#   num **= 2

# mul()
# mul()
# mul()
# print(num)
''' --- '''
# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, long_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {long_name}')


# def get_balance():
#     global balance
#     print(f'У вас на сету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

'''--'''

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age_control(dict_):
#     for key, val in dict_.items():
#         if val < 17:
#             print(f'{key}, извините, Вы не можете войти в клуб по age-control')
#         else:
#             print(f'{key}, Вы можете войти в клуб')

# age_control(a)

''' -- '''

# a = ['pipi', 'papa', 'mama']

# def list_Upper(list_):
#     b = [i.title() for i in list_]
#     return b

# print(list_Upper(a))
'''---'''

# azb_sogl = 'бвгджзйклмнпрстфхцчшщ'
# azb_gl = 'ауоыиэяюёе'

# def count_symbols(string):
#     sogl = 0
#     gl = 0
#     dr = 0

#     print(list(string.lower()))
#     for i in list(string.lower()):
#         if i in azb_gl:
#             gl +=1
#         elif i in azb_sogl:
#             sogl += 1
#         else:
#             dr += 1

#     print(f'Количество гласных: {gl}, согласных {sogl}, остальных символов: {dr}')
    
# print(count_symbols('Мурат супер!'))

'''---'''

# a = []

# def a_():
#     global a
#     for i in range(11):
#         a.append(i)

# a_()
# print(a)

'''reduce'''
# import functools 
# list_ = [1, 2, 3, 4]  
# result = functools.reduce(lambda x, y: x + y, list_) 
# print(result)
'''---'''
# import functools 
# list_ = [5, 6, 7, 8] 
# result = functools.reduce(lambda x, y: x * y, list_) 
# print(result)
'''---'''
# import functools 
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = functools.reduce(lambda x, y: x if len(x) > len(y) else y, list_) 
# print(result)
'''all'''
# list_ = [12, 3, 1, 23, 1, 2, 233]
# result = all(i > 3 for i in list_)
# print(result)

'''any'''
# list_ = [5, 8, 4, 6, 7]
# result = any(i < 0 for i in list_)
# print(result)
'''map(lambda())'''
# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x ** 2, list_))
# print(result)
'''---'''
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: False if x < 0 else True, list_))
# print(result)
'''---'''
# dict_ = {}
# result = dict(map(lambda x: (x[0], str(x[1])), dict_).items())
# print(result)

'''filter'''
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)
'''filter'''
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)
# '''filter'''
''''filter'''
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = list(filter(lambda x: x % 2 == 0, list_))
# list3 = list(filter(lambda x: x % 2 == 1, list_))
# result = f'even: {len(list2)}, odd: {len(list3)}'
# print(result)
'''---'''
# from random import choices
# from itertools import repeat
# from string import ascii_letters, digits


# inp = int(input('--> '))
# result = {
#     f(choices(ascii_letters, k=10), choices(digits, k=6))
#     for f in repeat(lambda x, y: ''.join(set(x+y)), inp)
# }
# print(result)

# from statistics import mean

'''---'''
# list2 = [i for i in list1 if type(i) == type(1) or type(i) == type(1.0)]
# list2 = [sqrt(i) for i in list2 if i > 0]

# num_list = [213, 5646, 43, 452]

# for i in num_list:
#     if len(str(i)) % 2 == 1:
#         print(f'число {i} - цифра по середине: {int(str(i)[len(str(i))//2])}')
#     else:
#         print(f'''число {i}:
#          цифры по середине: {int(str(i)[len(str(i))//2-1])} и {int(str(i)[len(str(i))//2])}''')

'''---'''
# students_ = {'Akmaral': 100,
#              'Yntymak': 43,
#              'Bilal': 86,
#              'Kutman': 65,
#              'Bayel': 54,
#              'Atay': 37,
#              'Yiman': 21,
#              'Eliza': 89,}
# dict_del = {k: v for k, v in students_.items() if v < 60}
# for k, v in dict_del.items():
#     print(f'Уважаемый студент {k}, вы набрали {v} баллов, что значит, вы не сможете больше продолжать обучение в нашем ВУЗе')
'''---'''
# import functools
# list_num_ = ['H','a','h','A','X','o']
# print(list_num_)
# string_ = functools.reduce(lambda x, y: x+y, list_num_)
# print(string_)
'''random'''
# import random
# print(random.choice())
'''def'''
# Функция высшего порядка - это функция, которая в качестве аргумента принимает любую функцию.
# Декоратор - функция, котoрая позволяет без изменения кода обернуть другyю функцию для того, чтобы 
# расширить функционал обернутой функции.

# def decorator(func):
#     print(func)
#     return func()
# def hello():
#     print('Ya hello :)')
#     return 'Hello'
# def john():
#     print('Ya john')
#     return 'John'
# print(hello())
# print()
# print(decorator(hello))
# print()
# print(decorator(john))

# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнения функции {func.__name__}, заняло {round(finish-start, 2)}')

# def loop():
#     i = 0
#     range_namber = 200000
#     while i <= range_namber:
#         print(i)
#         i += 1

# benchmark(loop)

# Pythonic way -> @benchmark
# Синтаксический сахар - это красота кода
'''Декоратор'''
# def benchmark(func):
#     def wrapper():        
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__}, заняло {round(finish-start, 2)}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_namber = 200000
#     while i <= range_namber:
#         # print(i)
#         i += 1

# @benchmark
# def add():
#     range_num = 200000
#     ls = []
#     for i in range(range_num):
#         ls.append(i)
#     # print(ls)


# add()
# loop()
''''''
# def strong(func):
#     def wrapper(*args, ** kwargs):
#         return '<str> ' + str(func()) + ' </strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div> ' + str(func()) + ' </div>'
#     return wrapper

# @strong
# @div
# @strong
# @div
# def get():
#     return 'Jhon Son'

# print(get())
''''''
# sogl = 'бвгджзйклмнпрстфхцчшщъь'
# gl = 'ауоыиэяюёе'
# def sim(str_):    
#     kol_s = 0
#     kol_g = 0
#     kol_o = 0
#     for i in list(str_.lower()):
#         if i in sogl:
#             kol_s += 1
#         elif i in gl:
#             kol_g += 1
#         else:
#             kol_o += 1
    
#     return f'Количество знаков: {len(str_)}\nКоличество согл: {kol_s}\nКоличество гл: {kol_g}\nКоличество других символов: {kol_o}'

# print(sim('Мой дорогой дневник, мне не описать ту боль и унижение'))

# azb_sogl = 'бвгджзйклмнпрстфхцчшщ'
# azb_gl = 'ауоыиэяюёе'

# def count_symbols(string):
#     sogl = 0
#     gl = 0
#     dr = 0

#     print(list(string.lower()))
#     for i in list(string.lower()):
#         if i in azb_gl:
#             gl +=1
#         elif i in azb_sogl:
#             sogl += 1
#         else:
#             dr += 1

#     print(f'Количество гласных: {gl}, согласных {sogl}, остальных символов: {dr}')
    
# print(count_symbols('Мурат супер!'))