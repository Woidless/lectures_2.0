''' try-except '''

# IndexError, ValueError, NameError, KeyError, ZeroDivisionError

# b = 10
# c = 11
# try:
#     print(a)
# except ZeroDivisionError:
#     print('Нет такой переменной')

# num1 = int(input())
# num2 = int(input())
# try:
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(result)
# dict_ = {'key1': 'value1', 'key2': 'value2'} 

# try:
#     print(dict_['key3'])
# except KeyError:
#     print('')
# try:
#     age = int(input())
#     if age < 18:
#         raise Exception('Доступ запрещен')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# inp1 = input()
# list_ = []
# list2 = inp1.split()
# print(list2)
# for i in list2:
#     try:
#         list_.append(int(i))
#     except:
#         raise ValueError('Данный элемент не является числом!')
    
# print(list_)


# inp1 = input()

# try:
#     list_ = []
#     list2 = inp1.split()
#     for i in list2:
#         list_.append(int(i))
#     print(list_)
# except:
#     raise ValueError('Данный элемент не является числом!')