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

# list_ = ['я любуюсь миром','лежу на боку']
 
# max_el = ''
# for el in list_:
#     list2 = el.split()
#     for el_inner in list2:
#         if len(max_el) < len(el_inner):
#             max_el = el_inner
    
# print(max_el)

'''-------------'''

"""
1) Создайте класс Languages.
В этом классе должен быть атрибут класса, который обозначает количество студентов,
изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса:
Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов,
изучающих тот или иной язык. При создании объекта-студента от одного из дочерних классов,
автоматически количество студентов в классах меняется. Если студент изучает язык Python,
то количество студентов должно увеличиться на один и в классе Python и в классе Languages.
Аналогично со студентами JavaScript.
Далее, в дочерних классах должен быть переопределен метод coding, в классе
Python он должен выдавать вам строку “I am Python student. I am coding now.”,
а в классе JavaScript - “I am JavaScript student. I am coding now”.
Создайте двух студентов от двух дочерних классов.
Далее программа сама рандомно выбирает студента и предлагает вам угадать,
какого студента она выбрала. После вашего выбора, он вызывает метод coding у
загаданного студента и выдает вам результат: если вы отгадали правильно,
пишет “Good job!”, если нет - “No bueno :(”
"""
# писать код здесь

# from random import choice

# class Languages:
#     students_py = 0
#     students_js = 0

# class Python(Languages):
#     students = 0
#     def __init__(self) -> None:
#         super().__init__()
#         Languages.students_py += 1
#         self.students += 1

#     def coding(self):
#         return 'I am Python student. I am coding now.'

# class JavaScript(Languages):
#     students = 0
#     def __init__(self) -> None:
#         super().__init__()
#         Languages.students_py += 1
#         self.students += 1

#     def coding(self):
#         return 'I am JavaScript student. I am coding now'

# py = Python()
# js = JavaScript()
# print(py.coding())
# print(js.coding())
# choice_ = choice(('py', 'js'))
# choice_2 = input('Как думаете, кого выбрали?: ')
# if choice_ == choice_2: print('Good job!')
# else: print('No bueno :(')

"""
2) Создайте свой класс MyList, который наследуется от list.
Переопределите метод списка insert(), который обычно принимает первым аргументом индекс,
а вторым - элемент. В своем классе MyList переопределите этот метод так,
чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс
"""
# писать код здесь
# class MyList(list):
#     def insert(self, __index, __object) -> None:
#         return super().insert( __object, __index)

# list_ = MyList([1, 4, 6, 8])
# list_.insert(2, -1)
# print(list_)

# -----------
# class MyMRO(type):
#     def mro(cls):
#         return (cls, A, B, X, Y, object)

# class C(A, B, metaclass = MyMRO):
#     pass

# obj1 = C()
# print(obj1.__mro__)

"""
1) Объявите абстрактный класс геометрических фигур Shape и определите в
нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.
Затем, наследуйте от Shape три класса: Triangle, Square и Circle.
треугольник создаётся с заданными основанием base и высотой height
квадрат создаётся с заданной длиной стороны length
круг создаётся с заданным радиусом radius
Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.
Затем, создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()
"""
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, height, base) -> None:
#         super().__init__()
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return (self.base * self.height) // 2


# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__()
#         self.lenght = lenght

#     def get_area(self):
#         return self.lenght ** 2

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__()
#         self.radius = radius
    
#     def get_area(self):
#         from math import pi
#         return pi * self.radius**2

# triangle = Triangle(4, 5)
# square = Square(6)
# circle = Circle(6)
# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())
"""
2)Создайте класс ContactList, который должен наследоваться от встроенного класса list.
В вашем классе должен быть реализован метод search_by_name,
который должен принимать имя и возвращать список всех совпадений.
Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.
Примерный ввод:
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":
['Ivan Olya', 'Olya Ivan'] 
"""
# class ContactList(list):
#     def __init__(self, list_: list):
#         self.list_ = list_
        
#     def search_by_name(self, name):
#         list_ = [i for i in self.list_ if name in i]
#         return list_

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 

    
"""
3)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World".
Затем, создайте класс B, который будет наследоваться от класса A.
Создайте экземпляр в переменной b1 от класса B, и через него вызовите метод method1.
"""
# писать код здесь
# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     pass

# b1 = B()
# b1.method1()

"""
4) Создайте класс Person который будет описывать человека, а точнее его
имя - name и возраст - age. Добавьте к классу метод display(), который будет выводить данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person.
Объекты от класса Student должны иметь все атрибуты, которые были определены
в родительском классе и еще один дополнительный атрибут - faculty, который будет описывать факультет, где учится студент.
Создайте метод display_student(), который будет выводить данные об этом студенте.
Создайте от класса Student объект в перемнной obj_student, и выведите данные о нём, как о человеке, затем как о студенте.
Например, применим методы к объекту obj_student:
obj_student.display() 
obj_student.display_student() 
допустим, у нашего объекта в атрибуте name хранится значение Rick, в age - 21,
а в faculty значение science, вывод в терминал должен быть:
name:Rick, age:21 
name:Rick, age:21, faculty:science 
"""
#писать код здесь
# class Person():
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age = age 

#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')

# class Student(Person):
#     def __init__(self, name, age, faculty) -> None:
#         super().__init__(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')


# obj_student = Student('Moon', 14, 'FIT')
# obj_student.display() 
# obj_student.display_student() 
class Terminal:
    def __init__(self, number: int, pin: int) -> None:
        if len(list(str(number))) != 16:
            raise ValueError('Номер должен содержать 16 цифр')
  
        if len(list(str(pin))) != 4:
            raise ValueError('Пин-код должен содержать 4 цифры')
        self.number = number
        self.__pin = pin
        self.money = 0

    def put(self, pin: int, money: int):
        if pin == self.__pin:
            self.money += money
            return f'На ваш баланс зачислено {money} сом'
        else:
            return 'Неверный пин-код'

    def get_money(self, pin: int, money: int):
        if pin != self.__pin: return 'Неверный пин код'
        if money % 10 != 0 and self.money < money: return 'Сумма некоректна'
        self.money -= money
        return f'С вашего баланса снято {money} сом'

terminal = Terminal(number = 1234567812345678, pin=4567)
print(terminal.put(4567, 1000))
print(terminal.put(456, 1000))
print(terminal.put(4567, 1000))
print(terminal.get_money(4567, 200))
print(terminal.money)