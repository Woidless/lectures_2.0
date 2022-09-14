"""
1)	В текстовом файле посчитать количество строк,
а также для каждой отдельной строки определить количество в ней символов и слов.
"""
#писать код здесь

# letters = 0
# lines = 0
# words = 0
# with open('file1.txt') as file:
#     line_of_file = file.readlines()
#     line_of_file = [line.replace('\n', '') for line in line_of_file]
#     lines = len(line_of_file)
#     for line in line_of_file:
#         words += len(line.split())
#         for i in line:
#             letters += 1

# print(f'letters: {letters}\nlines: {lines}\nwords: {words}')


"""
2) Откройте файл task3.txt в режиме записи. Запишите в него числа от 0 до 9 через символ *.
Затем вернитесь в начало файла и распечатайте записанные числа. Вывод должен быть:
0*1*2*3*4*5*6*7*8*9
"""
# писать код здесь
# with open('task3.txt', 'w+') as file:
#     file.write('0')
#     for i in range(1,10):
#         file.write(f'*{i}')
#     file.seek(0)
#     text = file.readline()
#     print(text)


"""
3)Откройте файл task2.txt. В нём записаны числа от 1 до 5 в столбец.
Распечатайте все числа, не используя методы.
Вывод в терминале должен быть:
1
2
3
4
5
"""
#писать код здесь

# with open('task2.txt', 'w+') as file:
#     [file.write(f'{i}\n') for i in range(1, 6)]
#     file.seek(0)
#     nums = file.read(9)
#     print(nums)


"""
4)Откройте файл task5.txt. В нём записаны целые числа. Прочтите эти числа, затем найдите максимальное затем минимальное число. Затем запишите эти числа в новый файл task6.txt через символ - (сначала минимальное, потом максимальное)
В файле task6.txt должна быть такая запись: 1-456 
"""
#писать код здесь

# with open('task5.txt', 'r')as file1, open('task6.txt', 'w')as file2:
#     nums = file1.read()
#     nums_int = list(map(int, nums.split()))
#     file2.write(f'{min(nums_int)}-{max(nums_int)}')


"""
5)Вам дан объект Python сохраненный в переменной python_obj и имеющий значение None.
Преобразуйте данный объект в формат JSON и сохраните в переменной json_obj.

Ввод должен быть:
  python_obj = None  
  #ваш остальной код 
  print(json_obj) 

Вывод:
  null 
"""
#писать код здесь
# import json
# python_obj = None
# json_obj = json.dumps(python_obj)
# print(json_obj)

"""
6)В task2.json хранятся данные в формате JSON.

Напишите программу Python которая будет считывать данные с файла и сохранять их в переменной json_obj.

Затем, преобразуйте это обьект в объект Python и запишите результат в переменную python_obj.
"""
#писать код здесь
# import json
# with open('task2.json') as file:
#     json_obj = file.read()
#     print(json_obj)
#     python_obj = json.loads(json_obj)
#     print(python_obj)