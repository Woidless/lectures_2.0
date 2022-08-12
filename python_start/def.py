''' функции (def) '''

# *args - кортеж позиционных аргументов
# **kwargs - словарь именнованных арументов (keyword arguments)

# def fun():
#     print('Hello')

# def get_string_length(string):
#     kol = 0
#     for i in list(string):
#         kol += 1
#     return kol

# print(get_string_length('hello'))

# dict_ = {'id': 2, 'email': 3}

# def dictionary(dictt):
#     for i in dictt.keys():
#         print(i)

# dictionary(dict_)

# def max_num(x, y):
#     if x > y:
#         return x
#     else:
#         return y

# print(max_num(6, 12))

# def multiply_list(list_):
#     prod = 1
#     for i in list_:
#         prod *= i
#     return(prod)
# print(multiply_list([i for i in range(1, 7)]))

# DRY ('Don\'t repeat youerself') - не повторяйся
'''  '''
# def send_message(email, message):
#     return f'{message} было отправлено на {email}'

# def notify_user(name):
#     message = input('Введите сообщение: ')
#     email = input('Введите почту: ')
#     note = send_message(email, message)
#     print(f'Здравствуйте, {name}. {note}')

# notify_user('Актан')

# def phonk(*args, **kwargs):
#     print('args: ', args)
#     print('kwargs: ', kwargs)

# phonk(1, 2, 3, 4, 5)
# phonk(k = 7, c = 23 )
'''---'''

# def phonk(*args):
#     counter = 0

#     for i in args:
#         try:
#             counter += i
#         except:
#             print(f'{i} не является числом')
        
#     return counter

# print(phonk(6, 7, 4, 8, 2, ' fsdfdsf', 5))