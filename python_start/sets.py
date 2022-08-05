''' Множества (set) '''

# множества - изменяемый, неупорядоченный тип данных.
# содержитт уникальные элементы и только неизменяемые типы данных.
# 

# a = {}
# print(type(a))

# b = set()
# print(type(b))

# c = {'a', 1, True, (1, 2), 2.54, None}
# print(c)

# d = {1, 1, 1, 1}
# print(d)

# e = {1, 2, [21, 12]}
# print(e) # ERROR

# list_ = [1, 1, 1, 2, 2, 2, 3]
# a = list(set(list_))
# print(a)

# from string import ascii_lowercase
# print(ascii_lowercase)

# from string import ascii_lowercase
# print(ascii_lowercase)

# alph = {'a': 1, 'b': 2, 'c': 3}
# print(alph)
# alph2 = {k: val for k, val in 'abcdefj' and range(len('abcdefj'))}

# stringascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

# dict_ = {}
# j = 0
# for i in stringascii_lowercase:
#     dict_[i] = j
#     j += 1
# print(dict_)
# alph = []
# for i in range(97, 123):
#     alph.append(chr(i)) 

# alph2 = {}
# for i in range(97, 123):
#     alph2.setdefault(chr(i), i - 96) 
# print(alph2)

# alph3 = {}
# for i in range(26):
#     alph3[]

# dict_ = {}
# num = 1
# for i in alph:
#     dict_[i] = ord(i) - 96
#     num += 1
# print(dict_)



# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#        'gmail.com': ['alena.semyonova', 'ivan.polekhin',["bhbmb", "bmhbbhb"], 'marina_abrabova'],
#        'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#        'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#        'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#        'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# list_ = []
# kol_in_one = []

# sum_kol = 0
# kol = 0
# for key, val in emails.items():
#     for i in range(len(val)):
#         if type(val[i]) == type(list()):
#             for j in range(len(val[i])):
#                 list_.append(val[i][j]+'@'+key)
#                 sum_kol += 1
#                 kol += 1
#         else:
#             list_.append(val[i]+'@'+key)
#             sum_kol += 1
#             kol += 1
#     kol_in_one.append(kol)
#     kol = 0

# print(kol_in_one)
# print(sum_kol)

# stat = {}
# i = 0
# for key in emails.keys():
#     stat[key]  = str((100 / sum_kol) * kol_in_one[i])+' %'
#     i += 1

# print(stat)

# print(list_)
