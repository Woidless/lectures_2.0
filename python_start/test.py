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

mon = 1000
print(f'У вас осталось {mon}$')

while mon > 0:

    summa = input('Введите сумму, к-ю хотите снять ')
    if not summa.isdigit():
        print('Пожалуйста, введите целые числа ')
        continue
    else:
        summa = int(summa)
        
    if summa > mon:
        print('Недостаточно средств ')
        break
    else:
        mon -= summa
    print(f'У вас осталось {mon}$')

print('Работа завершена')

