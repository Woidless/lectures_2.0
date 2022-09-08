'''
Задание 1
Создайте класс Class1 с 2 методами - first и second.
Создайте второй класс Class2, который наследуется от Class1,
и определите в новом классе Class2 ещё 2 метода - third и fourth.
Создайте экземпляр obj от класса Class2 и вызовите у него все четыре метода.
------
внутри методов прописывать и возвращать ничего не нужно,
можно просто оставить ключевое слово pass.
pass говорит Python что функция пока ничего не выполняет,
но в будущем возможно вы вернетесь и допишите туда код.
'''
# # class Class1():
#     def __init__(self):
#         pass
    
#     def first(self):
#         pass
    
#     def second(self):
#         pass

# class Class2(Class1):

#     def third(self):
#         pass
    
#     def fourth(self):
#         pass

# obj = Class2()

# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

'''
Задание 2
Создайте класс A и определите в нём метод method1,
который будет печатать строку

Основной функционал

Затем создайте второй класс B, который наследуется от класса A.
Внутри класса B переопределите method1 таким образом,
чтобы он помимо строки "Основной функционал", также печатал строку

Дополнительный функционал

Объявите экземпляр класса B в переменной obj и вызовите метод method1.
Результат в терминале должен быть:

Основной функционал 
Дополнительный функционал 
# '''
# class A():
#     def __init__(self):
#         pass

#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         A().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

'''
Задание 3
Создайте класс MyString, который будет наследоваться от str.
Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop.
Пример:
example = MyString('String') 
example.append('hello') 
print(example) 
Вывод в терминал будет:
Stringhello 
Применим метод pop() к объекту example:
print(example.pop()) 
print(example) 
cам метод возвратит нам удаленную строку, в терминале получим:
o 
Stringhell 
'''
# class MyString(str):

#     def __init__(self, string):
#         self.string = string

#     def append(self, to_end):
#         self.string = self.string + to_end 

#     def pop(self):
#         delete = self.string[-1]
#         self.string = self.string[:-1]
#         return delete
    
#     def __str__(self):
#         return self.string

# example = MyString('String') 
# example.append('hello') 

# print(example) 
# print(example.pop()) 
# print(example) 
'''
Задание 4
Создайте класс MyDict который будет наследоваться от встроенного класса dict.
Переопределите метод get() таким образом,
чтобы при попытке получения несуществующего ключа,
по умолчанию он возвращал, вместо None, строку:

Are you kidding?
Создайте экземпляр класса в переменной 'obj_dict' и
попробуйте получить несуществующий ключ методом get().

Например:

obj_dict = MyDict({'some_title': 2}) 
print(obj_dict.get('some')) 
Ключа 'some' в нашем словаре нет,
есть только 'some_title', в терминале получим:

Are you kidding? 
Метод get имеет такой синтаксис: словарь.get(ключ, значение),
в значение передается то что вы хотите возвратить если такого ключа не существует.
По умолчанию, если второе значение не передано, метод возвращает None.
Для переопределения метода унаследуйте метод от родителя и передайте в метод свое значение.
'''
# class MyDict(dict):

#     def get(self, key, default='Are you kidding?'):
#         return dict.get(self, key, default)

# obj_dict = MyDict({'some_name': 2})
# print(obj_dict.get('some')) 
'''
Задание 5
Создайте класс Person который будет описывать человека,
а точнее его имя - name и возраст - age. Добавьте к классу метод display(),
который будет выводить данные об этом человеке.

Создайте второй класс Student,
который будет наследоваться от класса Person.

Объекты от класса Student должны иметь все атрибуты,
которые были определены в родительском классе и
еще один дополнительный атрибут - faculty,
который будет описывать факультет, где учится студент.

Создайте метод display_student(),
который будет выводить данные об этом студенте.

Создайте от класса Student объект в перемнной obj_student,
и выведите данные о нём, как о человеке, затем как о студенте.

Например, применим методы к объекту obj_student:

obj_student.display() 
obj_student.display_student() 
допустим, у нашего объекта в атрибуте name хранится значение Rick, 
age - 21, а в faculty значение science, вывод в терминал должен быть:

name:Rick, age:21 
name:Rick, age:21, faculty:science 
'''
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'name:{self.name}, age:{self.age}'

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         person_dis = super().display()
#         return f'{person_dis}, faculty:{self.faculty}'
# obj_student = Student('Jorge', 20, 'FIT')
# print(obj_student.display())
# print(obj_student.display_student())
'''
Задание 6
Создайте класс ContactList,
который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name,
который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной
all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":

['Ivan Olya', 'Olya Ivan'] 
'''
# class ContactList(list):
#     def __init__(self, val=list()):
#         self.list = val

#     def search_by_name(self, contact):
#         list_ = [i for i in self.list if contact in i]
#         return list_


# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 
'''
Задание 7
Создайте класс SmartPhones, экземпляры класса должны иметь такие свойства:

name - название
color - цвет
memory - память
battery - процент заряда батареи
Значение battery по умолчанию должно быть 0.

Переопредилите метод str так чтобы при распечатке он выдавал строку
с названием и памятью смартфона.
У данного класса также должен быть метод charge,
который увеличивает значение батареи на указанную величину.
Создайте два дочерних класса от Smartphones:
Iphone - с дополнительным аттрибутом экземпляра - ios и
методом send_imessage(принимает в аргументы строку и возвращает эту строку и
от какого телефона сообщение было выслано в таком формате -
sending 'ваша строка' from 'название объекта-телефона')
Samsung - с дополнительным аттрибутом android и
методом show_time(который показывает текущее время)
Создайте объекты phone, iphone7, samsung21 от классов
SmartPhones, Iphone, Samsung и примените все методы.
Для правильной работы тестов, проделайте все следующие операции:
создайте объект от класса SmartPhones:
phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 
вывод:
generic 128GB
распечатайте свойство батарейки,затем примените метод charge(),
зарядив телефон до 20%:
print(phone.battery) 
phone.charge(20) 
print(phone.battery) 
получим в терминале:
0 
20 
создайте объект от класс Iphone, распечатайте этот объект,
и примените метод send_imessage:
iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 
вывод будет:
Iphone 7 128gb 
sending hello from Iphone 7 128gb 
создайте объект от Samsung и примените метод show_time():
samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 
вывод будет:
18:37:02.712036 
'''
# from datetime import datetime


# class SmartPhones:
    
#     def __init__(self, name, color, memory, battery=0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def __str__(self):
#         return f'{self.name} {self.memory}'

#     def charge(self, battery):
#         self.battery += battery
#         return self.battery

# class Iphone(SmartPhones):

#     def __init__(self, name, color, memory, ios, battery=0):
#         super().__init__(name, color, memory, battery)
#         self.ios = ios
        
#     def send_imessage(self, message):
#         return f'sending {message} from {self.name} {self.memory}'

# class Samsung(SmartPhones):

#     def __init__(self, name, color, memory, android, battery=0):
#         super().__init__(name, color, memory, battery)
#         self.android = android

#     def show_time(self):
#         return datetime.now().time()
        
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery)

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 

'''
Задание 8
Напишите класс CustomError который наследуется от
встроенного класса исключений Exception.

Переопределите __init__ таким образом чтобы через
экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса в переменной capitals_error с сообщением:

ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ
Напишите функцию check_letters(вне класса, отдельно от класса),
проверяющую строки на регистр и если строка не написана в верхнем
регистре выбросите исключение созданное классом CustomError:

Traceback (most recent call last):
  File "inheritance.py", line 121, in <module>
    check_letters(a)
File "inheritance.py", line 117, in check_letters
    raise capitals_error
main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ 
Если же все хорошо необходимо вывести сообщение: ВСЕ ОТЛИЧНО! {ваша строка}.

Например:

print(check_letters("HELLO")) 
Вывод будет:

ВСЕ ОТЛИЧНО! HELLO 
Если мы применим функцию к этой строке:

print(check_letters("hello")) 
Получим исключение от нашего класса CustomError:

Traceback (most recent call last): 
 File "inheritance.py", line 121, in <module> 
     check_letters(a) 
 File "inheritance.py", line 117, in check_letters 
     raise capitals_error 
__main__.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ 
'''
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
        
# def check_letters(string):
#     if string.isupper(): return f'ВСЕ ОТЛИЧНО! {string}'
#     else: raise capitals_error

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# print(check_letters("HELLO")) 