''' Условные выражения '''
# >
# <
# ==
# !=
# >=
# <=

# print(20 > 10)
# print(13 < 5)
''' if '''

''' else '''

''' elif '''

# if условие: 
#     действие
# elif другое_условие:
#     другое_действие
# else:
#     действие в случае ни одно из выше указанных условие не сработало

# s = 'fdf'
# s.isalpha()
# s.isalnum()
# s.isdigit()

# in - Проверка а вхождение
# string = 'Привет! как твои дела?'
# if 'привет' in string.lower():
#     print('yes')
# else:
#     print('no')

# in - Проверка а вхождение
# string = 'Привет! как твои дела?'
# if not 'привет' in string.lower():
#     print('no')
# else:
#     print('yes')

''' and, or, not '''
# False and False - False
# True and True - True
# False and True - False
# True and False - False

# True + True = 2
# a = 10 

# [действие1, действие2][условие]
#     0          1       1 или 0
# print(['ok', 'not ok'][a > 10]) # ok
''' Тернарный оператор '''
# a = ''
# msg = input('Введите сообщение: ')
# if len(msg) > 10:
#     a = 'Сообщение длинее 10 символов'
# else:
#     a = 'Сообщение меньше 10 символов'
# print(a)

# msg = input('Введите сообщение: ')
# print('Сообщение длинее 10 символов' if len(msg) > 10 else 'Сообщение меньше 10 символов')
# действие if условие else другое_действие


# col = input('Выбери цвет: ')

# match col:
#     case 'red':
#         print('Ok, red')
#     case 'white': 
#         print('Ok, white')
#     case 'black':
#         print('Ok, black')
#     case _:
#         print('We don\'t have this color')

# a = 'string'
# assert len(a) == 0
# print('It\'s ok')
f_num = int(input('sjdbfk'))
assert f_num == 30, 'число не верное'
print('число верное')