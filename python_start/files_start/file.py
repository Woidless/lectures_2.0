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


# ------------------------

from PIL import Image
import pytesseract
import re

def get_imei_codes(list_images):
    list_of_imei = []
    for image in list_images:
        str1 = pytesseract.image_to_string(image)
        print(str1)
        list_of_imei.append(re.findall(r'IME.\d.\s\d+', str1))
        print('!!!')
        print(list_of_imei)

    with open('imei_codes.txt', 'w') as my_file:
        for x in list_of_imei:
            for i in x:
                my_file.write(f'{i}\n')

ls = ['imei.jpg']
get_imei_codes(ls)