# name_of_list = ['Hello! Have a good day']
# new_list = [] 
# for i in name_of_list[0][len(name_of_list[0])//2:]:
#     new_list.append(i)
    
# for i in name_of_list[0][:(len(name_of_list[0]))//2]:
#     new_list.append(i)
 
# print(new_list)


# list_ = ['world', 'hello']
# new_list=[]
# for i in list_[::-1]:
#     new_list.append(i)
# print(new_list)

# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# print(suitcase)
# suitcase.pop()
# print(suitcase)
# suitcase.insert(0, 'панама')
# print(suitcase)


# list_ = []
# for i in range(0,101,2):
#     list_.append(i)
# print(list_)


# a = input()
# list_ = a.split(',')
# print(sorted(list_))

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# list_ = []
# for key, val in a.items():
#     if val == None:
#         a.pop(key)
# print(a)

# a1 = {1: 3}
# a2 = dict(gg = '5')
# a3 = dict.fromkeys(['c', 'g'])

# res = 1
# res *= 3
# print(res)

# list('makers')
# string = list("hello")
# dict_ = dict.fromkeys(string, 1)
# dict_['t'] = 2
# print(dict_)
# string = "pythonist"
# dict_ = {}
# for i in string:
#     dict_[i]
# dict_['t'] = 2
# print(dict_)

# string = "pythonist"
# string1 =list(string)
# i = 0
# dict_ = dict.fromkeys(string1, 1)
# for key in dict_:
#     i += 1
#     if i == 3:
#         dict_[key] = 2

# print(dict_)    

# Написать программу, которая будет запрашивать кол-во денег,
# к-ое вы хотите потратить. Если указанное число больше,
# чем денег в кошельке - программа предупреждает об этом и останавливается. 
# Иначе отнивает указанное число из кошелька о печатает кол-во оставшихся денег
# Если деньги заканчиваются - программа останавливается

# mon = 1000
# print(f'У вас осталось {mon}$')

# while mon > 0:

#     summa = input('Введите сумму, к-ю хотите снять ')
#     if not summa.isdigit():
#         print('Пожалуйста, введите целые числа ')
#         continue
#     else:
#         summa = int(summa)
        
#     if summa > mon:
#         print('Недостаточно средств ')
#         break
#     else:
#         mon -= summa
#     print(f'У вас осталось {mon}$')

# print('Работа завершена')
''' Кратное написание '''
# # loop
# my_list = []
# for i in range(50):
#     my_list.append(i)
# print(my_list)

# # list comprehension
# my_list2 = [i for i in range(50)]
# print(my_list2)
# #######
# # loop
# my_list3 = []
# for i in range(50):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list3)
'''  '''
# # list comprehension
# my_list4 = [i for i in range(50) if i % 2 == 0]
# print(my_list4)
'''  '''
# dictionary comprehension
# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# my_dict = {val: key for key, val in my_dict.items()}
# print(my_dict)
'''  '''
# list_ = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
# print(list_)

# n = int(input())
# dict_ = {i:i**2 for i in range(1, 501) if i % n == 0}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: [val for val in range(1, val + 1)]  for k, val in a.items()}
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {key: 'odd' if val % 2 == 1 else 'even' for key, val in dict_.items()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_.split() if i.isdigit()]
# print(list_)

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }

# new_dict = {key1: [key2 for key2 in val1.keys() if val1[key2] == max(val1.values())][0] for key1, val1 in dict_.items()}

# new_dict = {key1: [key2 for key2 in val.keys() if val[key2] == max(val.values())][0] for key1, val in dict_.items()}
# print(new_dict)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key: [val2 for val2 in val.values()][0] for key, val in my_dict.items()}
# print(dict_)

# dict_ = {2: 'string1', 1: 'str', 5: 'string112', 4: 'string12222'}
# dict_ = {key: len(val) if key % 2 == 0 else len(val)**3 for key, val in dict_.items()}
# print(dict_)

# fullset = set()
# for i in set1:
#     fullset.add(i)
# for i in set2:
#     fullset.add(i)

# set1 = {i for i in range(10)}
# set2 = {i for i in range(8, 18)}
# full_set = (set1 | set2)
# if len(full_set) == 20:
#     print('Ваш объединенный сет полностью уникальный!')
# else:
#     print(f'В этом сете было {(len(set1)+len(set2))-len(full_set)} повторения, его длина составляет {len(full_set)}')

# print(set1)
# print(set2)
# print(full_set)
'''  '''
# def foo():
#   var = 'переменная foo'
#   print('переменная в foo: ', var)                
  
#   def bar():
#     global var
#     var = 'переменная bar'
 
#   bar()

# foo()
# print('переменная в foo: ', var)
'''  '''
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу измениться'
# my_func()
# print(x)
'''  '''
# num = 3 

# def mul():
#   global num
#   num **= 2

# mul()
# mul()
# mul()
# print(num)
'''  '''
