''' Кортеж(tuple) '''
# Кортеж - неизменяемая последовательность элементов.
# Введет себя как список, но не изменяется

# print(dir(tuple))



# my_tuple = (1, 2, 3, 4, 5)
# # print(type(my_tuple)) - tuple
# a = (2)
# # print(type(a)) - int
# b = ('strint', )
# # print(type(b)) - tuple
# c = [1, 2 ,3], 'string', 3
# # print(type(c)) - tuple

# num = 1
# num1 = 2
# num2, num3 = 4, 7
# print(num2, num3)

# tuple2 = ('str1', 'str2', 'str3')
# print(*tuple2)
# print(tuple2)


''' Распаковка '''
# nums = (10, 5)
# print(pow(*nums))

# a, b, *c= 1, 2, 3, 4
# print(a)
# print(b)
# print(c)


# new_tuple = (('name','Alina'),
# ('name', 'Marina'),
# ('name', 'Kayrat'),
# ('name', 'Mirbek'))

# for i in new_tuple:
#     print(i)

# for key, val in new_tuple:
#     print(key)
#     print(val)

''' функции для последовательностей '''

# len(последовательность) - возвращает кол-во элементов в последовательностти
# max(последовательность)
# min(последовательность)
# sum(последовательность)


# numbers = (3, 4, 5, 7, 32)
# counter_ = 0
# for num in numbers:
#     counter_ += num
# print(counter_)

# t = (1, 2, 4)
# t = list(t)
# print(t)

# a = [1, 2, 3]
# b = (1, 2, 3)
# print(a.__sizeof__())
# print(b.__sizeof__())