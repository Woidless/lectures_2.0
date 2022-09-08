'''
Задание 1
Напишите декоратор call_function,
который печатает перед вызовом полученной функции строку:
Вызываю функцию <имя_функции>
Затем следует вызов функции.
После вызова функции должна печататься строка:
"Вызов функции <имя_функции> прошёл успешно"
Ввод:
@call_function
def first():
    print("hello world")
    return "hello world"
first()
Вывод:
Вызываю функцию first
hello world 
Вызов функции first прошёл успешно 
'''
# def call_function(func): 
#     def wrapper(): 
#         print(f"Вызываю функцию {func.__name__}") 
#         func() 
#         print(f"Вызов функции {func.__name__} прошёл успешно") 
#     return wrapper 
        
# @call_function
# def first(): 
#     print("hello world") 
#     return 'hello world' 
# first()

'''
Задание 2
Создайте декоратор func_start_time,
который будет распечатывать дату и время вызова принимаемой функции,
а затем вызывает саму функцию, например:

@func_start_time
def func():
    print('Hello world')
func()
Вывод:

Функция запущена 26.02.2021 21:51
Hello World
Для этого воспользуйтесь модулем datetime.
'''
# def func_start_time(func):
#     def wrapper(*args, **kwargs): 
#         import datetime
#         time_ = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
#         print(f"Функция запущена {time_}") 
#         return func(*args, **kwargs)
#     return wrapper

# @func_start_time
# def func():
#     print("Hello world")

# func()
'''
Задание 3
Создайте 3 декоратора, каждый из которых применяет
к тексту определённый стиль:
выделение жирным <b>...</b> (декоратор make_bold)
курсив <i>...</i> (декоратор make_italic)
подчеркивание <u>...</u> (декоратор make_underline)
Далее создайте функцию hello которая будет возвращать текст
Hello world
примените к этой функции цепочку декораторов.
@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello world'
print(hello())
Вывод должен быть:
<b><i><u>Hello world</u></i></b>
'''
# def make_bold(func):
#     def wrapper(): 
#         return(f'<b>{func()}</b>')
#     return wrapper

# def make_italic(func):
#     def wrapper(): 
#         return(f'<i>{func()}</i>')
#     return wrapper

# def make_underline(func):
#     def wrapper(): 
#         return(f'<u>{func()}</u>')
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello(): return 'Hello world'

# print(hello())
'''
Задание 4
Создайте декоратор benchmark, замеряющий время выполнения функции
в секундах и выводящий строку например:
Время выполнения: 0.05 секунд.
Затем объявите функцию fetch_webpage,
которая выполняет GET-запрос на главную страницу Google,
оберните в декоратор и вызовите её:

@benchmark 
def fetch_webpage(): 
  import requests 
  webpage = requests.get('https://google.com')  
'''
# import time

# def benchmark(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         print(f'Время выполнения: {(time.time() - start_time)} секунд')
#     return wrapper

# @benchmark 
# def fetch_webpage(): 
#     import requests 
#     webpage = requests.get('https://google.com')  

# fetch_webpage()
'''
Задание 5
Создайте словарь users и сохраните в нем несколько пользователей
(ключом будет имя пользователя, а значением пароль пользователя).
Напишите следующую функцию:
def login(username, password):
    print(f'Welcome, {username}')
Допишите к этой функции декоратор validate_password,
который будет проверять есть ли в словаре пользователь с
таким username и совпадает ли пароль.
Если такого username нет, то функция должна выводить сообщение:
Username is not defined 
Если же не совпадает password, т.е username сохранен с другим значением password,
выведите сообщение:
Password is invalid 
'''
# users = {'klark': 231, 'Flamingo': 953}

# def validate_password(func):
#     def wrapper(username, password):
#         acc = users.get(username, 'Username is not defined')
#         if acc == password: func(username, password)
#         elif acc == 'Username is not defined': print(acc)
#         elif acc != password: print('Password is invalid')

#     return wrapper

# @validate_password 
# def login(username, password): 
#     print(f'Welcome, {username}')
    
# login('klark', 231)
'''
Задание 6
Напишите функцию get_user,
принимающую в аргументы словарь вида:
get_user({'username': 'john133', 'is_admin': True})
напишите также декоратор is_admin,
который проверяет является ли юзер админом,
если да выведите сообщение:
Доступ разрешен john133
если же юзер не админ:
Доступ запрещен john133
input:
@is_admin
def get_user(dict):
    return dict
get_user({'username': 'john133', 'is_admin': True})
get_user({'username': 'jane133', 'is_admin': False})
Доступ разрешен john133
Доступ запрещен jane133
'''
# def is_admin(func):
#     def wrapper(dict):
#         if dict['is_admin']: print(f'Доступ разрешен {dict["username"]}')
#         else: print(f'Доступ запрещен {dict["username"]}')
#     return wrapper
    

# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})
'''
Задание 7
Вам дана функция get_page(path),
которая принимает в аргументы путь к
определенной странице вашего вебсайта(https://www.mywebsite.com/).
Напишите декоратор route,
который будет выводить абсолютный путь(url), к какой-либо странице:
Например, если передадим строку '/about' или '/products' в нашу функцию:
@route
def get_page(path):
    return path
print(get_page('about/'))
print(get_page('products/'))
После обработки декоратора, получим такой результат:
https://www.mywebsite.com/about/
https://www.mywebsite.com/products/
'''
# def route(func):
#     def wrapper(path):
#         return f'https://www.mywebsite.com/{path}'
#     return wrapper

# @route
# def get_page(path):
#     return path

# print(get_page('about/'))
# print(get_page('products/'))
'''
Задание 8
Напишите функцию prefix_name, которая принимает в аргументы список,
состоящий из кортежей:
name_format([('Leo', 'Nimoy', 40, 'M'),
('Carrie', 'Fisher', 35, 'F'),
('Harrison', 'Ford', 38, 'M')])
В каждом кортеже, через запятую хранится
имя, фамилия, возраст и пол человека - 'M' - мужской, 'F' женский.
Функция должна возвращать строку - 'Ms. Carrie Fisher',
с приставкой Ms. если это человек женского пола, и с приставкой Mr.
если мужского - 'Mr. Leo Nimoy'.Также напишите декоратор sort_names,
который возвратит осортированный по возрасту список имен(по возрастанию):
Ввод:
def sort_names(func):
     ...
@sort_names
def prefix_name(person):
     ...
print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
                   ('Carrie', 'Fisher', 35, 'F'),
                   ('Harrison', 'Ford', 38, 'M')]))
Вывод должен быть:
['Ms. Carrie Fisher', 'Mr. Harrison Ford', 'Mr. Leo Nimoy']
'''
    # person = sorted(person, key= lambda age: age[2])


# from curses.ascii import isdigit
# def sort_names(func):
#     def wrapper(lst):
#         list_of_lists = [i for i in func(lst)]
#         list_of_lists = sorted(list_of_lists, key= lambda obj: int(obj[-1]))
#         return [' '.join(i[:-1]) for i in list_of_lists]
        
#     return wrapper

# @sort_names
# def prefix_name(person):
#     list_ = []
#     for sets in person: 
#         if 'M' in sets:   string = 'Mr. '
#         else:             string = 'Ms. '
#         sets = list(map(str, sets))
#         for s in sets: 
#             if s not in 'MF': string += s + ' '

#         list_.append(string.split())
#     return list_
    
# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#                    ('Carrie', 'Fisher', 35, 'F'),
#                    ('Harrison', 'Ford', 38, 'M')]))
'''
Задание 9
Напишите функцию sort_phone_nums которая принимает
список телефонных номеров в виде строк:
sort_phone_nums(['0700987456', '0555123456', '0770369852'])
функция должна отсортировать по возрастанию список номеров и
разделить их символом #.
Напишите декоратор get_full_number,
который преобразует телефонные номера в sort_phone_nums,
добавляя к ним региональный код +996 и убирая лишний ноль в начале номера:
+996 555 123456
+996 770 369852
+996 777 987456
Ввод:
def get_full_number(func):
    ...
@get_full_number
def sort_phone_nums(list_):
    ...
sort_phone_nums(['0777987456', '0555123456', '0770369852'])
Вывод:
+996 555 123456#+996 770 369852#+996 777 987456
'''
# def get_full_number(func):
#     def wrapper(list_):
#         print('#'.join(func(list_)))
#     return wrapper

# @get_full_number
# def sort_phone_nums(list_):
#     list_ = sorted([int(num[1:]) for num in list_])
#     list_ = list(map(str, list_))
#     list_ = ['+996 '+i[:3]+' '+i[3:] for i in list_]
#     return list_

# sort_phone_nums(['0777987456', '0555123456', '0770369852'])
'''
Задание 10
Напишите декоратор type_check() который принимает в
аргументы тип данных - str, int, list, dict и.т.д и
проверяет подходит ли аргумент декорируемой функции по типу данных,
к примеру, если у нас есть функция func1:
@type_check(int)
def func1(num):
    print(num*2)
наш декоратор приняв в аргументы int,
должен проверить что аргумент функции num принадлежит именно типу данных int:
func1(2)
возвратит результат 4, если же передадим другой тип данных, к примеру словарь:
func1({1: 'какой-то', 2: 'словарь'})
декоратор возвратит строку:
Неверный тип данных :(
Ввод:
def type_check(correct_type):
    ...
@type_check(int)
def func1(num):
    print(num*2)
func1(2)
func1({1: 'какой-то', 2: 'словарь'})
Вывод:
4
Неверный тип данных :(
'''
# def type_check(correct_type):
#     def wrapper(func):
#         def wrapper2(func_arg):
#             if type(func_arg) == correct_type:
#                 func(func_arg)
#             else: print('Неверный тип данных :(')
#         return wrapper2
#     return wrapper

# @type_check(int)
# def func1(num):
#     print(num*2)
# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})