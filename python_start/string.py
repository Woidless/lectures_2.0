"""Строки (string)"""

# Строки - неизменяемый, упорядоченный, индексируемый тип данных
 
# string1 = "hello"
# string2 = 'hello'
# doc_string1 = """Для документации
# классная тема
# советую"""
# doc_string2 = '''Тоже самое
# только другой знак
# тоже советую'''

# string3 = 'I\'m Bilal '
# Конкатенация - склеивание строк/сложение строк
# print(string1 + string3)

# print(string1 * 3)

'''Функции и методы строк'''
# my_str = 'my besto friendo'
# # print(len(my_str)) - выводит длину строки
# # print(my_str.split('separator')) - делит по указанному делителю (по умолчанию - пробел)
# # my_str2 = my_str.replace('e', 'a') # My basto friando - заменя подстроки в строке
# my_str.upper() # MY BESTO FRIENDO - перевод в верхний регистр
# my_str.lower() # my besto friendo - перевод в нижний регистр
# my_str.title() # My Besto Friendo - перевод первого символа каждого слова в верхний регистр
# my_str.capitalize() # My besto friendo - перевод в верхний регистр первого символа строки
# 'спец символ'.casefold() #  переводит спец символ/ более агрессивный перевод в нижний регистр
# my_str.count('e') # 2 - считает количество вхождений переданной подстроки
# ''' Индексы и срезы '''
# str7 = 'good morning'
# Индекс - порядковый номер символа в подстроке
#     'makers'
#    0 1 2 3 4 5
# # -6-5-4-3-2-1
# print(str7[-12])
# # print(str7[start:stop:step])

# print(str7.find('ood')) # поиск индекса подстроки в строке
# print(str7.index('mor')) # поиск индекса подстроки в строке
# print('*'.join(['ola','kepasso','fdfsf'])) #-  соединяет переданный список строк по указанной строке




# str8 = '   my name is   '
# print(str8)
# print(str8.strip()) - убирает указанный символ в строке с двух сторон (по умолчанию - пробел)
# print(str8.lstrip) - убирает пробелы слева
# print(str8.rstrip) - убирает пробелы справа
# print(str8)
# ''' Методы проверки '''
# string = 'My test string 123'

# print(string.isdigit())
# print(string.isalpha())
# print(string.isalnum())
# print(string.isspace())
# print(string.islower())
# print(string.isupper())
# print(string.endswith('123'))
# print(string.startswith('My'))


# num1 = 10
# num2 = 20
# str1 = 'apple'
# str2 = 'hello'
# print(str1 > str2)
# ord('a')
# chr(97)
# # ASCII
# a = 'jsbdjsbd'
# b = 'nsdns'
# print(sorted(a))
# print(sorted(b))

''' Форматирование/интерполяция строк '''
# stat = 'привет, Фархат! Приглашаю тебя на праздник'

# name = 'Bilal'
# place = 'ChaiHana'
# # %
# str5 = 'Привет, %s! Приглашаю тебя на праздник' % name
# print(str5)
# # format
# str6 = 'Привет, {}'.format(name)
# print(str6)
# str7 = f'Привет, {name}! Приглашаю тебя в {place}'
# print(str7)
# Форматирование строк - подстановка переменных в строку, созданние динамической строки
# a = 'I\'m student'
# b = 'Идет бычек качается,\n\tВздыхает на ходу'
# print(b)
# # \n - newline 
# # \t - tabular
# str8 = r'This is a test string\n\t\n'
# print(str8)
# # r - raw
# windows_path = 'User\Doc\\new_folder'
# print(windows_path)

''' Оператор in '''
# string = 'Hello world'
# string2 = 'ell'
# print(string2 in string)

# str1 = 'hello'
''' помощник для каждого типа данных '''
# dir(object)
# print(dir(12))
# name = input('Name ')
# last_name = input('Last_name ')
# age = int(input('age '))
# city = input('City ')
# print(f'Привет {name} {last_name}, вам {age} лет, вы живете в {city}')
# x = int(input())
# y = int(input())
# if x / y > x // y:
#     print(f'x не делится на y\nЧастное: {x // y}\nОстаток: {x % y}')
# else:
#     print(f'x делится на y\nЧастное: {x // y}')
# print((1, 2, 3)< (1,2,4))