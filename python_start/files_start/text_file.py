# with open('task1.txt', 'r') as file:
#     lines = file.readlines(9)
#     for line in lines:
#         print(line)
'''---'''
# with open('task.txt') as file:
#     for line in file:
#         print(line)
'''---'''
# with open('task.txt', 'w+') as file:
#     for i in range(10):
#         file.write(f'{i}*')
#     file.seek(0)
#     print(file.read())
'''---'''
# with open('task4.txt', 'r') as file:
#     kol = (len(file.readlines()))
#     print(kol)
'''---'''
# import functools

# with open('/home/bilal/makers_l/python_start/files_start/task5.txt', 'r') as file:
#     list_ = [int(el) for el in file]
#     max_ = functools.reduce(lambda x,y: x if x > y else y, list_)
#     min_ = functools.reduce(lambda x,y: x if x < y else y, list_)

# with open('/home/bilal/makers_l/python_start/files_start/task6.txt', 'x') as file1:
#     file1.write(f'{min_}-{max_}')
'''---'''
