# ООП инкопсуляция
'''
public - password
protected - _password
private - __password
'''

'''
Задание 1
Создайте класс A и объявите в нём 3 метода:
публичный(public) (возвращает строку 'Public method'),
защищённый(protected) (возвращает строку 'Protected method')
приватный(private) (возвращает строку 'Private method')
Затем создайте экземпляр в переменной obj1 данного класса и вызовите
(с выводом в терминал) по очереди каждый из методов.
Не забудьте, что нужно вызвать приватный метод так, чтобы ошибка не выводилась
'''
# class A():
#     def __init__(self):
#         pass
#     def public(self):
#         return 'Public method'
#     def _protected(self):
#         return 'Protected method'
#     def __private(self):
#         return 'Private method'
# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

'''
Задание 2
Определите класс A, в нём объявите метод method1, который печатает строку "Hello World".
Затем, создайте класс B, который будет наследоваться от класса A.
Создайте экземпляр в переменной b1 от класса B, и через него вызовите метод method1.
'''
# class A():
#     def __init__(self):
#         pass 
#     def method1(self):
#         print('Hello World')
# class B(A):
#     def __init__(self):
#         pass
# b1 = B()
# b1.method1()

'''
Задание 3
Объявите класс Car, в котором будет приватный атрибут экземпляра класса speed.
Затем, определите метод set_speed, который будет устанавливать
значение скорости и метод show_speed, который возвращает значение скорости.
Создайте экземпляр в переменной car1 класса Car и вызовите все методы.
Ввод:
car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed()) 
Вывод:
0 
20 
'''
# class Car():
#     __speed = 0
#     def set_speed(self, speed):
#         self.__speed = speed
#     def show_speed(self):
#         return self.__speed
# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 
'''
Задание 4
Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter,
а метод show_speed() с использованием декоратора @property.
Создайте обьект car1 класса Car.
Ввод:
car1 = Car() 
print(car1.speed) 
car1.speed = 20 
print(car1.speed) 
Вывод:
0 
20 
'''
# class Car():
#     __speed = 0
#     @property
#     def speed(self):
#         return self.__speed
#     @speed.setter
#     def speed(self, speed):
#         self.__speed = speed
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)
'''
####################################
Read - only
'''
# class CoorWriteError(Exception):
#     pass
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#     @property
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self, v):
#         raise CoorWriteError('x coor read only')
#     @property
#     def y(self):
#         return self._y
#     @y.setter
#     def y(self, v):
#         raise CoorWriteError('y coor read only')
# point = Point(12, 5)
# print(point.x)
# print(point.y)
# point.x = 20
'''
####################################
write-read
'''
# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius
        
#     @radius.setter
#     def radius(self, val):
#         self._radius = val

#     @property
#     def diam(self):
#         return self._radius * 2

#     @diam.setter
#     def diam(self, val):
#         self._radius = val / 2

# circle = Circle(7)

# print(circle.radius)
# print(circle.diam)

# circle.diam = 50
# print(circle.diam)
# print(circle.radius)
'''
####################################
write - only
'''
# import hashlib
# import os

# class User:
#     def __init__(self, name, password):
#         self.username = name
#         self.password = password

#     @property
#     def password(self):
#         raise Exception('Password write only')

#     @password.setter
#     def password(self, password):
#         if not isinstance(password, str):
#             raise Exception('Invalid value for password')
#         salt = os.urandom(32)
#         self._hashed_password = hashlib.pbkdf2_hmac('sha256',
#                                                     password.encode('utf-8'),
#                                                     salt,
#                                                     100_000)

# jhon = User('Bakr', '1234')
# print(jhon.username)
# # print(jhon.password)
# jhon.password = '567'
# print(jhon._hashed_password)
