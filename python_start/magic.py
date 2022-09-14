'''
magic methods
dunder methods -(double underscore) - __init__
служебные методы
'''
# res = 5 + 5 # __add__
# print(res.imag)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

'''
МАГИЧЕСКИЕ МЕТОДЫ СРАВНЕНИЯ
'''

'''
__eq__(self, other) -> ==
__ne__(self, oter) -> !=
__lt__(self, other) -> <
__gt__(self, other) -> >
__le__(self, other) -> <=
__ge__(self, other) -> >=
'''

# class Word(str):
#     def __new__(cls, word):
#         print(word)
#         word = word.replace(' ', '')
#         print(word)
#         return super().__new__(cls, word)

#     def __init__(self, word) -> None:
#         self.word = word

#     def __gt__(self, __x: str) -> bool:
#         print('сработал __gt__')
#         print('\t'+'!'*10, self, '\t'+'!'*10)
#         print('\t'+'!'*10, __x, '\t'+'!'*10)
#         return len(self) > len(__x)

#     def __lt__(self, other: str) ->bool:
#         print('сработал __lt__')
#         return len(self) < len(other)

#     def __eq__(self, other: str) -> bool:
#         print('Jhon Snow')
#         return len(self) == len(other)

# obj = Word('wer     e')
# obj2 = Word('weresr')
# print(obj2 > obj)
# print('='*100)
# print(obj2 < obj)
# print('='*100)
# print(obj2 == obj)

'''
Конструктор -> __new__
Инициализатор -> __init__
'''
# class Conventer(float):
#     def __new__(cls, x):
#         print('New сработал!!!')
#         print('\t'+'!'*10, cls, '\t'+'!'*10)
#         print('\t'+'!'*10, x, '\t'+'!'*10)
#         if x < 50: raise Exception('x <<< 50')
#         return super().__new__(cls,x)

#     def __init__(self, number) -> None:
#         print('+'*10, self)
#         self.number = number

# print('='*100)
# print(obj3 := Conventer(100))

##########

# class Human():
#     def __new__(cls, stroka):
#         print( 'stroka\t' + stroka + '\t!!!')
#         return super().__new__(cls)


#     def __init__(self, stroka):
#         self.stroka = stroka

# print(obj := Human('Alpha'))
# print(obj1 := Human('Omega'))
# print(obj.stroka)
# print(obj1.stroka)
########

'''
Дандер методы для срокового оторажения объектов 

__str__ -> для отображения строки, которую будут видеть пользователи 
__repr__ -> строковую информацию как создавать экземпляр от класса
'''

# class Base:
#     def __init__(self, string) -> None:
#         self.string = string
    
#     def __str__(self)-> str:
#         return f'Объект: {self.string}'

#     def __repr__(self) -> str:
#         return f'Base("{self.string}")'

# print(word := Base('rerere'))
# print(word)
# print(repr(word))
# print(word3 := eval(repr(word)))
####
# class User:
#     def __init__(self, name, email) -> None:
#         self.name = name
#         self.email = email

#     def __str__(self) -> str:
#         return f'{self.name} -> {self.email}'

# print(user := User('Alina', 'Alena@mail.ru'))
#######
'''
+ - / * // % **
'''
# class Cifra(int):
#     def __new__(cls, number):
#         print('New')
#         instance = super().__new__(cls, number)
#         if not 0 < number < 100: raise ValueError('Введите число от 0 до 100')
#         return instance

#     def __init__(self, number):
#         self.number = number

#     def __add__(self, other):
#         print('add!')
#         print(f'result: {self} + {other} = {self.number + other}')
#         return self.number + other


# print(cifra := Cifra(13) + 17)
# # cifra = Cifra(15)
# print(cifra)
# print(cifra + 13)
 
'''
__sub__ -
__mul__ *
__floordiv__ //
__div__ /
__mod__ %
'''
# from curses import wrapper


# class User:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self):
#         print(f'User object: {self.name}')
#         self.hello = 'Hello World'

# user1 = User('Noone')
# user2 = User('Savage23')
# print(callable(user1))
# print(callable(user2))
# user1()
# print(user1.hello)

# class LogSetfile:
#     def __init__(self, file) -> None:
#         self.file = file

#     def __call__(self, func):
#         def wrapper (*args, **kwargs):
#             with open(self.file, 'a') as file:
#                 file.write(f'Func name: {func.__name__}\n')
#             return func(*args, **kwargs)
#         return wrapper

# test = LogSetfile('text.txt')
# print(callable(test))
# @test
# def start_test():
#     pass

# @test
# def hello():
#     pass

# @test
# def world():
#     pass

# a = test(start_test)
# a()
# start_test()
# hello()
# world()

# class Student(dict):
#     def __init__(self, point) -> None:
#         self.point = point

#     def __gt__(self, other)->bool:
#         print('self: ', sum(self.point.values())//3)
#         print('other: ', sum(other.point.values())//3)
#         return sum(self.point.values())//3 > sum(other.point.values())//3

# obj1 = Student({'math': 89, 'bio': 100, 'phisic': 98})
# obj2 = Student({'math': 67, 'bio': 76, 'phisic': 87})
# obj3 = Student({'math': 95, 'bio': 86, 'phisic': 100})

# print(obj1 > obj2)
# print(obj2 > obj1)
# print(obj1 > obj2)

# x = {'math': 89, 'bio': 100, 'phisic': 98}
# print(x.values())

# class MyList(list):
#     def __init__(self, ls) -> None:
#         self.ls =ls

#     def __getitem__(self, index):
#         print(self.ls[index - 1])

# x = MyList([1, 2, 3, 4, 5])
# x[1]
# x[3]

# class Copilka:
#     def __init__(self) -> None:
#         self.__total = 0
#         self.__coins = []

#     def add_coin(self, coin):
#         self.__total += coin
#         self.__coins.append(coin)

#     @property
#     def total(self): return self.__total

#     def __len__(self): return len(self.__coins)

#     def __getitem__(self, index): return self.__coins[index]

#     # def __

# obj = Copilka()

# obj.add_coin(coin=30)
# obj.add_coin(coin=36)
# obj.add_coin(coin=37)
# obj.add_coin(coin=38)

# print(obj.total)
# print(len(obj))
# print(dir(obj))
# print(x := [i for i in obj])

# class Car:
#     def __init__(self) -> None:
#         self.model = 'Honda'

#     def __delattr__(self, name) -> None:
#         value = getattr(self, name)
#         print(f'{name} = {value} removed!')
#         super().__delattr__(name)

#     # def __str__(self) -> str:
#     #     return f'{self}'

# print(a := Car())

# print(a.model)
# del a.model

# class Person:
#     def __init__(self, atters) -> None:
#         for k, v in atters.items():
#             # print(self, k ,v)
#             setattr(self, k, v)
    
#     # def __str__(self) -> str:
#     #     return dict(self)

# obj = Person({'name': 'Naruto', 'income': 180000, 'eyes': 'blue'})
# obj2 = Person({'email': 'Ichigo@g,ain.com', 'last_name': 'Kurosake', 'eyes': 'brown'})

# print(f'{obj.name} -> {obj.income}')