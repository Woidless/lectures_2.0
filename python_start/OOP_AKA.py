'''
Ассоцияция Композиция Агрегация
Все эти три понятия очень похожи друг на друга. Все они означают,
что внутри одного оъекта будет существовать другой 
'''

'''Композиция'''

# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type} - Jhon Snow'

# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# room = Room()

# print(room.west_wall)
# print(room.east_wall)
# print(room.south_wall)
# print(room.north_wall)

'''Ассоциация'''

# class Stream:
#     def __str__(self) -> str:
#         return 'Jhon\'s stream'

# class Logger:
#     def __init__(self) -> None:
#         self.stream = None

#     def print_the_stream(self):
#         if self.stream: print(f'Stream from class: {self.stream}')
#         else: print('None stream')

# logger = Logger()
# logger.stream = Stream()
# logger.print_the_stream()

'''Агрегация'''

# class Stream:
#     def __str__(self) -> str:
#         return 'Stream object'

# class Logger:
#     def __init__(self, stream) -> None:
#         self.stream = stream

#     def print_the_stream(self):
#         if self.stream: print(f'Stream from class: {self.stream}')
#         else: print('None stream')

# print(log := Logger(Stream()))
# log.print_the_stream()

# 

# class Engine:
#     country = 'Germany'
#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Country: {self.country} -> Engine: {self.power}.'

# class Car:
#     model = 'Audi'
#     country = 'Germany'

#     def __init__(self, type, power) -> None:
#         self.engine = Engine(power)
#         self.type = type

#     def __str__(self) -> str:
#         return f'{self.model} {self.type} -> Engine: {self.engine} -> {self.country}'

# print(car := Car('A8', 665))

'''
class methods, instance methods, static methods

Методы экземпляра класса (Instance methods) - это те методы в ООП, к-ые изменяют состояние экземпляра класса:
def method(self) - self ссыдка на экземпляр

Методы класса(class methods) - это те методы, к-ые могут изменять состояние самого класса и манипулировать самим классом:
@class method # декоратор, к-ый определяет метод класса
def method(cls) -- cls это ссылка н асам класс

Статические методы (Static methods) - это те методы, к-ые не могут изменять состояния на экземпляра от класса ни самого класса:
@staticmethod # декоратор, к-ый определяет статик метод
def method()
'''
# def likes(*names):
#     if names: print(*names)
#     else: print('no names')

# likes('a', 'b', 'c')

'''Class methods'''
# class Student:
#     school_name = 'BC'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name, self.age, 'School: ', Student.school_name)

#     @classmethod
#     def change_school(cls, name):
#         print('!'*10, cls, '?'*10)
#         cls.school_name = name


# stud = Student('no', 12)
# stud.show()
# stud.change_school('ABC')
# stud.show()


'''Static methods'''
class Person:
    surnamae = 'Stark'
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        if age >= 18: print('Adult')
        else: print('Not Adult')

    @classmethod
    def from_birth_date(cls, name, year):
        from datetime import date
        cls.surnamae = 'Lancer'
        age = date.today().strftime('%Y:%M:%d')
        print(age)
        return cls(name, age)

jhon = Person('jhon', 19)
print(jhon.name, jhon.surnamae)
Person.is_adult(jhon.age)
jhon.is_adult(17)

jam = Person.from_birth_date('Jam', 1982)
print(jam.name, jam.age)

# class ClassMixin:
#     @classmethod
#     def method(cls):
#         print(cls)

# class Person(ClassMixin):
#     pass

# jhon = Person()
# jhon.method()
# ClassMixin.method()
# Person.method()
