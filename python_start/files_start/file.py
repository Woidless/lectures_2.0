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
# ------------------------

# from PIL import Image
# import pytesseract
# import re

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         str1 = pytesseract.image_to_string(image)
#         print(str1)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', str1))
#         print('!!!')
#         print(list_of_imei)

#     with open('imei_codes.txt', 'w') as my_file:
#         for x in list_of_imei:
#             for i in x:
#                 my_file.write(f'{i}\n')

# ls = ['imei.jpg']
# get_imei_codes(ls)


"""
1) Создайте файл numbers.txt и напишите скрипт,
который запишет в этот файл числа от 1 до 20.
Затем создайте файл squares.txt. Напишите скрипт,
который будет считывать числа из файла numbers.txt и
записывать квадраты этих чисел в файл squares.txt
"""
# писать код здесь
# with open('numbers.txt', 'w+') as file1, open('squares.txt', 'w+') as file2:
#     for i in range(1,21):
#         file1.write(f'{i}\n')
#     file1.seek(0)
#     list_nums = [i.replace('\n', '') for i in file1.readlines()]    
#     for i in list_nums:
#         file2.write(f'{int(i)**2}\n')

"""
2) Создайте файл usernames.txt.
Напишите скрипт, который будет запрашивать у пользователя имена,
а эти имена будут помещаться в файл usernames.txt.
При этом напротив каждого имени будет записано количество букв в юзернейме.
Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""
# писать код здесь

# with open('usernames.txt', 'a+') as file:
#     while True:
#         name = input('Введите имя: ')
#         if name.lower() == 'end':
#             break
#         file.write(f'Имя:\t{name}\tКол-во букв:\t{len(name)}\n')
'''---'''
# with open('numbers.txt','w+') as file, open('squares.txt','w+') as file2:
#     [file.write(f'{num}\n') for num in range(1,21)]
#     file.seek(0)
#     [file2.write(f'{int(i.replace("n", ""))**2}\n') for i in file.readlines()]
'''---'''
# with open('numbers.txt','w+')as file:
#     for number in range(1, 21):
#         file.write(f'{number}\n')
#     file.seek(0) # возвращает курсор в начало
#     with  open('squares.txt','w+')as file2:
#         list_of_str = file.readlines() # создает список,
#         # элементами которого явл каждая строка файла
#         print(list_of_str)
#         list_of_nums = [int(i.replace('\n', '')) for i in list_of_str] # заменяет в каждом элементе \n на пустоту
#         # затем делает из стринга в интеджер
#         print(list_of_nums)
#         for i in list_of_nums: 
#             file2.write(f'{i**2}\n') # записывает каждый элемент листа
#             # и возводит в квадрат добавляя \n
'''home-work'''
# Имеется файл file.txt с текстом на латинице.
# Напишите программу, которая выводит следующую статистику по тексту:

# количество букв латинского алфавита;
# число слов;
# число строк.

# INUT file.txt:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# OUTPUT
# 108 letters
# 20 words
# 4 lines

# letters = 0
# words = 0
# lines = 0
# with open('file.txt') as file:
#     list_of_lines = [i.replace('\n', '') for i in file.readlines()]
    
#     for line in list_of_lines:
#         lines += 1
#         words += len(line.split())

#         for i in line:
#             if i.isalpha():
#                 letters += 1

# print(f'{letters} letters\n{words} words\n{lines} lines')
'''---'''