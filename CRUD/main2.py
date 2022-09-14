from views2 import *

def main():
    while True:
        print('Что вы хотите сделать?\n(1-show_data, 2-create, 3-update, 4-get_on_product)')
        ch = input('Введите комманду: ')
        if ch == '1': print(show_data())
        elif ch == '2': print(create_product())
        elif ch == '3': print(update_product())

main()