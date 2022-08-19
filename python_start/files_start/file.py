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
1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и записывать квадраты этих чисел в файл squares.txt
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
2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""
# писать код здесь

# with open('usernames.txt', 'a+') as file:
#     while True:
#         name = input('Введите имя: ')
#         if name.lower() == 'end':
#             break
#         file.write(f'Имя:\t{name}\tКол-во букв:\t{len(name)}\n')