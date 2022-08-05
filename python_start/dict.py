''' словари '''
# словарь - изменяемый, итерируемый. Состоят из пар:
# ключ: значение. Клюючи могут быть тольько неизменяемые типы данных
# (tuple, str, int, None, bool), а значения - любые


# dict_ = {}
# passport = {
#     'name': 'Bilal',
#     'last_name':'Abd',
#     'age': 19,
#     'gender': 'pokemon',
#     'birthday': '23.02.2003'
#     }

# print(passport['name'])
# print(passport['last_name'])
# print(passport['age'])
# print(passport['gender'])
# print(passport['birthday'])

# dict2 = dict(name = 'Aman', last_name = 'Bol', age = 19, gender = 'pokemon', birthday = '23.02.2003')

# dict3 = dict.fromkeys(['a', 'b'], 25)
# print(passport)
# print(dict_)
# print(dict2)
# print(dict3)

# dict4 = dict.fromkeys(['a', '5']) # ([], None)

# dict5 = dict([('name', 'Moon'), ('last_name', 'light'), ('age', 23), ('gender', 'pokemon'), ('birthday', '23.03.2003')])



'''----'''


# dict_ = {}
# passport = {
#     'name': 'Bilal',
#     'last_name':'Abd',
#     'age': 19,
#     'gender': 'pokemon',
#     'birthday': '23.02.2003'
#     }

# print(passport.get('name'))
# print(passport.get('ida'))
# dict.get(key, None) - щтдает значение указанного ключа,
# если нет _ отдает второе указанное значение
# (по умолчанию)

# print(passport.get('id', 'Нет такого ключа'))

# passport.setdefault(key, None) - отдает занчение указанного ключа
# если его нет - создает со значением dafault(по умолчанию None)
# passport.setdefault('age') # 23
# print(passport.setdefault('id', 34444))
# print(passport)

# passport.update({key: value}) - принимает в себя другой словарь и 
# обновляет исходный за счет него


# dict8 = {
#     'name': 'Lalib',
#     'last_name':'Abd',
#     'age': 19,
#     'gender': 'pokemon',
#     'birthday': '23.02.2003' 
#     }
# passport.update(dict8)
# print(passport)


# a = {'a': 11, 'b': 22}
# a['c'] = 33
# print(a)



# dict10 = {
#     'name': 'Lalib',
#     'last_name':'Abd',
#     'age': 19,
#     'gender': 'pokemon',
#     'birthday': '23.02.2003' 
#     }
# dict10.pop('name')
# print(dict10)

# print(dict10.pop('id', 'Нет такого ключа'))
# print(dict10)

# it = dict10.items()
# print(it)
''' Методы '''

# get(key, None)

# clear()

# copy()

# pop(key, default)

# popitem()

# setdefault(key, default)

# update()

# dict1 = {1: 'Tom', 2: 'Alice'}
# dict2 = {1: 'Tom', 2: 'Alice'}

# fromkeys(seq, value = None)
 
# nums = [1,2,3,4,5]
# new_d = dict.fromkeys(nums, 'M')
# print(new_d)

# items(), keys(), values()

list_ = ['x--', '--x', '++x', 'x++']

x = 0

for i in list_:
    if '--' in i:
        x -= 1
        print(x)
    elif '++' in i:
        x += 1
        print(x)
        