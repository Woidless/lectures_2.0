'''
Задание 1
Создайте класс Account и переопределите в нем методы
__init__, __repr__, __str__ и __del__.
Объекты класса должны содержать атрибуты:
name - имени держателя счета
balance - баланса
city - города, где открыт счет
Переопределенные методы:
__init__ должен также выводить сообщение "Счет создан"
__repr__ должен возвращать имя держателя счета и баланс
__str__ должен возвращать сообщение 'Hello' и также информацию о держателе счета:
"Hello 'name' 'balance' 'city'" где вместо 'name', 'balance' и
'city' должны быть соответствующие значения атрибутов объекта.
__del__ должен выводить сообщение "Пока"
Создайте обьект класса obj_account с параметрами
('Rick', 2013, 'Bishkek') и вызовите все методы.
Ввод должен быть:
obj_account = Account("Rick", 2013, 'Bishkek')  
print(obj_account)  
print(repr(obj_account)) 
А вывод:
Счет создан   
Hello Rick 2013 Bishkek 
Rick 2013  
Пока 
'''
# class Account:
#     def __init__(self, name, balance, city) -> None:
#         print('Счет создан')
#         self.name = name
#         self.balance = balance
#         self.city = city

#     def __repr__(self) -> str:
#         return f'{self.name} {self.balance}'

#     def __str__(self) -> str:
#         return f'Hello {self.name} {self.balance} {self.city}'

#     def __del__(self):
#         print('Пока')

        
# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account)) 
'''
Задание 2
Определите класс MyNumber который наследуется от класса int.
У экземпляра класса должен быть обязательный атрибут value.
Переопределите методы сложения, вычитания,
умножения и деления для класса таким образом чтобы
при использовании операторов + - * /, результат возвращался с сообщением:
"Это сложение и результат равен: x"   
      #для оперетора + 
"Это вычитание и результат равен: x"  
      #для '-'   
"Это умножение и результат равен: x"  
      #для '*' 
"Это деление и результат равен: x"  
      #для '/' 
где вместо x должен быть результат вычислений.
Создайте обьект от класса MyNumber в переменной obj_int cо значением равным 5.
Примените все операторы по порядку +,-,*,/.
Ввод должен быть:
obj_int = MyNumber(5)  
print(obj_int + 5)  
print(obj_int - 5)  
print(obj_int * 5)  
print(obj_int / 5)  
Вывод:
Это сложение и результат равен: 10  
Это вычитание и результат равен: 0  
Это умножение и результат равен: 25  
Это деление и результат равен: 1.0 
'''
# class MyNumber(int):
#       def __init__(self, value) -> None:
#             self.value = value

#       def __add__(self, x):
#             print(f'Это сложение и результат равен: {self.value + x}')
#             return self.value + x

#       def __sub__(self, x):
#             print(f'Это вычитание и результат равен: {self.value - x}')
#             return self.value - x

#       def __mul__(self, x):
#             print(f'Это умножение и результат равен: {self.value * x}')
#             return self.value * x

#       def __truediv__(self, x):
#             print(f'Это деление и результат равен: {self.value / x}')
#             return self.value / x

# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)  

'''
Задание 3
Напишите класс MyList, который наследуется от list.
Сделайте так, чтобы индексация элементов начиналась с 1.
Создайте обьект obj_list и проверьте работоспособность программы.
Ввод должен быть:
obj_list = MyList([1,2,3,4,5])  
print(obj_list[1])  
А вывод:
1 
'''
# class MyList(list):
#       def __init__(self,mylist): 
#             self.mylist = mylist 
#       def __getitem__(self, index): 
#             return self.mylist[index-1]
# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])  

'''
Задание 4
Напишите класс Student, который описывает студента.
У студента есть следующие атрибуты: имя(name), класс(class_name),
и оценки(ball) по предметам в виде словаря, в следующем виде:
{’math’: 100, ‘history’: 89, literature’: 88}.
Переопределите методы сравнения >, < ,>=, <= так, чтобы сравнение студентов между
собой производилось по средней оценке студента по предметам.
Создайте два обьекта от класса Student в переменных obj_student1 и obj_student2.
Сравните эти два объекта знаками >, < ,>=, <=, и распечатайте результат.
Ввод у вас должен быть:
obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
print(obj_student1 > obj_student2)  
print(obj_student1 < obj_student2)  
print(obj_student1 >= obj_student2)  
print(obj_student1 <= obj_student2)  
Вывод должен быть в виде строки:
> False 
< False 
>= True 
<= True 
'''
# class Student:
#       def __init__(self, name: str, class_name: str, ball: dict) -> None:
#             self.name = name
#             self.class_name = class_name
#             self.ball = ball
      
#       def __gt__(self, other)->bool:
#             res = sum(self.ball.values())//len(self.ball.values()) > sum(other.ball.values())//len(other.ball.values())
#             return f'> {res}'

#       def __lt__(self, other)->bool:
#             res = sum(self.ball.values())//len(self.ball.values()) < sum(other.ball.values())//len(other.ball.values())
#             return f'< {res}'

#       def __ge__(self, other)->bool:
#             res = sum(self.ball.values())//len(self.ball.values()) >= sum(other.ball.values())//len(other.ball.values())
#             return f'>= {res}'

#       def __le__(self, other)->bool:
#             res = sum(self.ball.values())//len(self.ball.values()) <= sum(other.ball.values())//len(other.ball.values())
#             return f'<= {res}'

# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)  
'''
Задание 5
Напишите класс Word и переопределите методы 'больше чем', 'меньше чем',
'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len).
Также в методе __new__ напишите условие для удаления пробелов и пустых строк в созданных словах.
Создайте обьекты word1 и word2 класса Word и сделайте сравнения.
Ввод:
word1 = Word('H  e  l  l  o')  
word2 = Word('world!')  
print(word1 > word2)  
print(word1 < word2)  
print(word1 >= word2)  
print(word1 <= word2) 
Вывод должен быть:
False  
True  
False  
True 
'''
# class Word(str):
#       def __new__(cls, string):
#             if ' ' in string: string = string.replace(' ', '')
#             return super().__new__(cls, string)

#       def __init__(self, string: str) -> None:
#             self.string = string
            
#       def __gt__(self, other)->bool:
#             print(self)
#             print(other)
#             return len(self) > len(other)

#       def __lt__(self, other)->bool:
#             return len(self) < len(other)

#       def __ge__(self, other)->bool:
#             return len(self) >= len(other)

#       def __le__(self, other)->bool:
#             return len(self) <= len(other)

# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2) 
'''
Задание 6
Создайте класс Kopilka, у экземпляров класса должны быть приватные атрибуты:
total - общее количество накопленных монет, изначально равно 0
coins список монет которые были брошены в копилку, изначально пуст - [].
Добавьте метод add_moneta, который принимает аргумент moneta, и увеличивает
total на данное значение, а также добавляет монету в список coins.
Переопределите в классе магические методы __len__ и __getitem__ таким образом,
чтобы при применении функции len к объекту выдавалось количество монет в списке coins,
а при попытке перебора объекта класса циклом for, печатались монеты из списка.
Создайте объект obj от класса Kopilka, вызовите все методы класса, примените функцию len()
и переберите объект циклом for.
Ввод должен быть:
obj = Kopilka() 
obj.add_moneta(25) 
obj.add_moneta(30)
print(len(obj) 
for i in obj: 
     print(i) 
А вывод:
2 
25 
30 
'''
# class Kopilka:
#       def __init__(self) -> None:
#             self.__total = 0
#             self.__coins = []

#       def add_moneta(self, moneta):
#             self.__total += moneta
#             self.__coins.append(moneta)

#       @property
#       def total(self): return self.__total

#       def __len__(self):
#             return len(self.__coins)

#       def __getitem__(self, index):
#             return self.__coins[index]

# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30)
# print(len(obj))
# for i in obj: 
#      print(i) 
'''
Задание 7
Создайте класс Anagram который наследуется от класса str.
Переопределите магический метод отвечающий за сравнение так чтобы,
знак == сравнивал объекты класса, строки, на то являются ли они анаграммами или нет.
Также переопределите магический метод с помощью которого можно размножить строки:
2 * "hello" обычно возвращает "hellohello", сделайте так чтобы результат возвращался
в обратном порядке как: "olleholleh"
Создайте экземпляры класса в переменных word1 и word2, сравните их оператором == и
размножьте word1 на 3.
Ввод должен быть:
word1 = Anagram('hello') 
word2 = Anagram('olleh') 
print(word1 == word2) 
print(word1 * 3) 
Вывод:
True 
olleholleholleh
'''
# class Anagram(str):
#       def __init__(self, string) -> None:
#             self.string = string

#       def __eq__(self, __x) -> bool:
#             return self.string == __x[::-1]

#       def __mul__(self, other):
#             return (self.string * other)[::-1]

# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2) 
# print(word1 * 3) 
