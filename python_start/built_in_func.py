# map(func, iterable object)

# get_keys = lambda x: x.keys()
# dict_ = {1:'1', 2: '2'}
# print(get_keys(dict_))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6,7,8,9]
# print(get_last(ls=ls))

# def my_func(n):
#     return lambda a: a*n

# my_doubler = my_func(2)
# my_tripler = my_func(3)

# print(my_doubler(3))
# print(my_doubler(11))
# print(my_tripler(3))
# print(my_tripler(5))

# proj = lambda x, y: x* y
# print(proj(4, 6))
'''---'''
# def increment(x):
#     x += 1
#     return x

# def counter(num):
#     return lambda: increment(num)
# c = counter(0)
# print(c())
'''----'''

# dict_ = {'a': 12277, 'b': 234, 'c': 23442, 'd': 34233}
# new_dict = sorted(dict_.items(),
#                   key=lambda x: x[1])
# print(dict(new_dict))
'''---'''
# ls = ['safsd', 'vcxvc', 'lflflflf', 'kkfkfkfkf']
# new_list = sorted(ls, key=len)
# print(new_list)
'''---'''
# def func(string_: str)-> bool:
#     if len(string_) >= 4:
#         return True
#     return False

# x = lambda str1: len(str1) >= 4
# '''---'''
# ls = ['asda','asd534a','asa','ada','a2sda','asa',]

# # res = list(filter(func, ls))

# # res1 = list(filter(x, ls))
# # print(res, res1)

# x = dict(enumerate(ls))
# print(x)

# for  i, x in enumerate(ls):
#     print(i, x)
'''zip()'''
# zip(iterables) - она соединяет каждый элемент
# итеруемых объектов между собой в тип данных tuple
# и возвращает его

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [10, 20, 30, 40, 50]
# ls3 = [-1, -2, -3, -4 ]
# ls4 = [100, 200, 300, 400, 500]

# res = list(zip(ls1, ls2, ls3, ls4))

# print(res)

'''all'''
# list_ = [12, 3, 1, 23, 1, 2, 233]
# result = all(i > 3 for i in list_)
# print(result)

'''any'''
# list_ = [5, 8, 4, 6, 7]
# result = any(i < 0 for i in list_)
# print(result)
'''---'''

# from math import sqrt
# list1 = [False, 12, 432, -213, 23.43, 'ffewf']
# print(f' список до преобразования: {list1}')

# используется фильтер, чтобы оставить только числа
# list1 = list((filter(lambda x: type(x) == type(1) or 
#                                type(x) == type(1.0),
#                     list1)))


# здесь тоже используетмя фильтр на 26 линии дла положительных чисел
# затем находим квадрат каждого элемента
# list1 = list(map( lambda x: round(sqrt(x), 2),
#                   list(filter(lambda x: x > 0, list1))))

# print(f' список после преобразования: {list1}')

