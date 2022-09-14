from views1 import *

print('Что вы хоите делать? post, get, delete, put, detail')

while True:
    operation = input('Введите действие: ')
    if operation == 'get': [print(get_data()[i]) for i in range(len(get_data()))]
    elif operation == 'detail': print(get_one_data()) 
    elif operation == 'post': print(post_data())
    elif operation == 'put': print(update_data())
    elif operation == 'delete': print(delete_data())
    else: print('command not found')