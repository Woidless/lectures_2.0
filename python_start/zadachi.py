# list_ = ['x--', '--x', '++x', 'x++']

# x = 0

# for i in list_:
#     if '--' in i:
#         x -= 1
#         print(x)
#     elif '++' in i:
#         x += 1
#         print(x)

'''---'''

list_ = ['я любуюсь миром','лежу на боку']
 
max_el = ''
for el in list_:
    list2 = el.split()
    for el_inner in list2:
        if len(max_el) < len(el_inner):
            max_el = el_inner
    
print(max_el)