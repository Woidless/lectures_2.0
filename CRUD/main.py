from views import *

def main():
    print('''Привет, тебе доступны следующие функции
    list-1\tretrieve-2\tcreate-3\tupdate-4\tdelete-5''')
    choice_ = input('input command: ')  
    if choice_ == '1':
        list_of_prods()
    elif choice_ == '2':
        detail_retrieve()
    elif choice_ == '3':
        create_product()
    elif choice_ == '4':
        update_prod()
    elif choice_ == '5':
        delete_prod()
    else:
        print('нет команды')
    
    ask = input('continue?(yes/no)')
    if ask.lower() == 'yes':
        main()
    else:
        print('Programm stoped')

main()