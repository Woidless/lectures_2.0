# num1 = int(input())
# num2 = int(input())
"""Математические операторы"""

# num1 + num2 # - сложение
# num1 - num2 # - вычитание
# num1 * num2 # - умножение
# num1 / num2 # - деление -> float()
# num1 ** num2 # - возведениие в степень
# num1 // num2 # - деление -> int()
# num1 % num2 # - деление -> int()

from decimal import Decimal
import imp
dec1 = Decimal('0.1')
dec2 = Decimal('0.1')
dec3 = Decimal('0.1')
# print(dec1 + dec2 + dec3)

""" Функции """
# abs() - возвращает модуль переданного числа / число без учета знака
# pow(2, 3) - возведение в степень
# pow(2, 3, 4) - возведение в степень, затем остаток от деления
# divmod(1, 2) - 1 // 2, 1 % 2 - (0, 1) 
# round(2.3456, 2) - оругление переданного числа до целого, если указан 'y',
# то округление до 'y' знаков после запятой
# import math # библиотека для мат. расчетов
# math.sqrt(25) # 5
# math.factorial(5) # 120
# print(math.pi)
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
print('Результат: ', num1 + num2)