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
# 'makers'
#  012345
# # -6-5-4-3-2-1
# print(str7[-12])
# # print(str7[start:stop:step])
# print(str7.find('ood')) # поиск индекса подстроки в строке
# print(str7.index('mor')) # поиск индекса подстроки в строке
# print('*'.join(['ola','kepasso'])) -  соединяет переданный список строк по указанной строке
str8 = '   my name is   '
# print(str8)
# print(str8.strip()) - убирает указанный символ в строке с двух сторон (по умолчанию - пробел)
# print(str8.lstrip) - убирает пробелы слева
# print(str8.rstrip) - убирает пробелы справа
print(str8)