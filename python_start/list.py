''' списки и циклы '''

# list()
# Список - изменяемый, упорядоченный, индексиуемый, итерируемый тип данных.
# Нужен для хранения нескольких элементов

# Элементами списка могут быть любый типы данных

# list_ = [2, 'dsa', True, False, [1, 2], None, {'a: 12'}, {1, 2}, ('a', 'b', 'c')]
# print(list_)
# list1 = []
# list2 = []

# list1.append(element)

# list1.insert(index, element)

# list1.extend(list2) добавляет все элементы list2 в list1


''' сортировка списка '''
# nums = [1, 3 ,4, 54]

# nums.sort()
# print(nums)
# str_ = ['h', 'c', 'r', 'b']
# str_.sort()
# print(str_)
# name_list = ['Aigerim', 'Bakha', 'Uluk', 'aizhan']
# name_list.sort(key=len)
# name_list.sort(reverse=True)
# print(name_list)

# sorted(name_list, key=len, reverse=True)

'''  '''
# my_list = ['h', 'c', 'r', 'b']
# my_list.reverse()
# print(my_list)

''' циклы '''

# Цикл - многократное выполнение определенного участвка кода

# for 
# Итерация - повтороенеи какого либо действия

# for - цикл работает до тех пор, пока элементы витерируемом объекте не заканчиваются
# for элемент in итерируемый_объект:
            # Тело цикла

# types_list = [int, str, list, bool, None, set, dict, tuple]
# iter_objs = []
# non_iter_objs = []
# for obj in types_list:
#     if '__iter__' in dir(obj):
#         iter_objs.append(obj)
#     else:
#         non_iter_objs.append(obj)
# print(iter_objs)
# print(non_iter_objs)
