''' Область видимости '''

# LEGB
# local - локальная
# Enclosed - замкнутая
# Global - шлобальная
# Built-in - встроенная

# область видимости - часть программы,
# где будет доступмно то или иное имя
# (переменная, функция, класс и тд)

# Имена из локальной области недоступны в глобальной
# области, но в локальной области доступны
# имена из глобальной области

# x = 20 # global

# def func_outer():
#     x = 15 # nonlocal

#     def func_inner():
#         x = 25 # local
#         print(x)
    
#     func_inner()

# func_outer()

# globals(), locals()

# locals() - показывает дочтупные имена той области,
# в которой была вызваниа


# print(dir(__builtins__))

# def func_(a, b, c):
#     return a + b + c

# nums = (3, 2, 5)
# dict_ = {'a': 3, 'b':4, 'c':3}

# print(func_(*nums))
# print(func_(**dict_))

# def my_func(x, y):
#     print('Before return')
#     return x + y
#     print('After return')

# my_func(3, 5)

# def func():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
