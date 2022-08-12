'''
r - read
r+ - read + write
w - write
w+ - read + write
a - append
a+ - append
x - write
----------
b - binary
t - text
'''
from math import sqrt
list1 = [False, 12, 432, -213, 23.43, 'ffewf']
print(f' список до преобразования: {list1}')

# используется фильтер, чтобы оставить только числа
list1 = list((filter(lambda x: type(x) == type(1) or 
                               type(x) == type(1.0),
                    list1)))


# здесь тоже используетмя фильтр на 26 линии дла положительных чисел
# затем находим квадрат каждого элемента
list1 = list(map( lambda x: round(sqrt(x), 2),
                  list(filter(lambda x: x > 0, list1))))

print(f' список после преобразования: {list1}')
