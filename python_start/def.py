''' функции (def) '''

# def fun():
#     print('Hello')

# def get_string_length(string):
#     kol = 0
#     for i in list(string):
#         kol += 1
#     return kol

# print(get_string_length('hello'))

# dict_ = {'id': 2, 'email': 3}

# def dictionary(dictt):
#     for i in dictt.keys():
#         print(i)

# dictionary(dict_)

# def max_num(x, y):
#     if x > y:
#         return x
#     else:
#         return y

# print(max_num(6, 12))

def multiply_list(list_):
    prod = 1
    for i in list_:
        prod *= i
    return(prod)
print(multiply_list([i for i in range(1, 7)]))