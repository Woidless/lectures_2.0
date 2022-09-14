"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий,
и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус.
Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса,
переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# from math import pi

# class Circle:
#     color='blue'
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return self.radius**2 * pi

# circle = Circle(12)
# print('цвет ДО переопределения:', circle.color)
# circle.color = 'red'
# print('цвет ПОСЛЕ переопределения:', circle.color)
# print('AREA:', circle.get_area())
"""
2) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона.
Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""
# class Book:
#     def __init__(self, name, last_name, telephone):
#         self.name = name
#         self.last_name = last_name
#         self.telephone = telephone

#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.telephone}'

# contact = Book('Billi', 'Betson', '+98888646')
# print(contact.get_info())

"""
3) Создайте класс HrDepartment с переменными класса recruiter и staff.
Экземпляр класса принимает параметры: name и last_name кандидата.
Добавьте в класс функции: 
- hire, которая увеличивает количество staff и возвращает сообщение с
приветствием нового сотрудника: “{имя} {фамилия}, welcome on board!”, и
- get_colleague с параметром colleague, в который попадает второй кандидат и
автоматически становится коллегой первого кандидата. Эта функция ничего не должна возвращать.

a. Создайте три экземпляра класса: candidate1, candidate2 и candidate3. 
b. Вызовите функцию hire у трех кандидатов и распечатайте результаты
c. Вызовите функцию get_colleague и распечатайте два сообщения:
“My name is {имя первого кандидата}. {имя второго кандидата} is my colleague” и наоборот: 
“My name is {имя второго кандидата}. {имя первого кандидата} is my colleague”
d. Распечатайте 1 сообщение: “I am recruiter {имя рекрутера}. I hired today {кол-во всего нанятых сотрудников} new staff”
"""
# class HrDepartment():
#     recruiter = 'Supermen'
#     staff = 0

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
    
#     def hire(self):
#         HrDepartment.staff += 1
#         return f'{self.name} {self.last_name}, welcome on board!'

#     def get_colleague(self, colleague):
#         self.colleague = colleague
#         colleague.colleague = self
    
#         print(f'My name is {self.name}. {colleague.name} is my colleague')
#         print(f'My name is {colleague.name}. {self.name} is my colleague')

# candidate1 = HrDepartment('Klark', 'Kent')
# candidate2 = HrDepartment('Alfred', 'Malino')
# candidate3 = HrDepartment('Very', 'Well')
# print(candidate1.hire())
# print(candidate2.hire())
# print(candidate3.hire())
# candidate1.get_colleague(candidate2)
# print(f'I am recruiter {candidate1.recruiter}. I hired today {candidate1.staff} new staff')

"""
4) Дан словарь: 
a = {1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation'}.

Создайте класс PythonCourse, параметр экземляра которого принимает словарь a.
Добавьте в класс функцию learn, которая добавляет в этот словарь новый элемент.
Создайте объект от PythonCourse, вызовите функцию learn и распечатайте сам объект. 
Например, если добавить элемент с ключом 5 и значением ‘Abstraction’, на выходе мы получим:
{1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation', 5: 'Abstraction'}
"""
# a = {1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation'}

# class PythonCourse():
#     def __init__(self, dict_):
#         self.dict_ = dict_

#     def learn(self, k, v):
#         self.dict_[k] = v

# obj = PythonCourse(a)
# print(obj.dict_)
# obj.learn(5, 'Abstraction')
# print(obj.dict_)
"""
1) Напишите программу по следующему описанию. Есть класс "Снайпер".
От него создаются два экземпляра. Каждому устанавливается здоровье в 100 очков.
В случайном порядке они стреляют друг в друга. Тот, кто стреляет, здоровья не теряет.
У того, в кого стреляют, оно уменьшается на 20 очков от одного выстрела.
После каждого выстрела надо выводить сообщение, какой снайпер атаковал,
и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья,
программа завершается сообщением о том, кто одержал победу.
"""
# писать код здесь
# from random import choice
# class Snipre:
#     hp = 100
#     def __init__(self, name):
#         self.name = name

#     def shot(self, player):
#         player.hp -= 20
#         print(f'{self.name} атаковал {player.name}.\nHP({player.name}={player.hp})')

# player1 = Snipre('Jhon')
# player2 = Snipre('Poll')
# while True:
#     player1.shot(player2) if choice(range(2)) else player2.shot(player1)
#     print('-'*50)
#     if player1.hp <=0:
#         print(f'{player2.name} Выйграл')
#         break
#     elif player2.hp <=0:
#         print(f'{player1.name} Выйграл')
#         break
# print('Программа завершена')
    

"""
2) Напишите программу по следующему описанию. Есть класс Hogwarts.
В нем определены следующие атрибуты-факультеты: 
Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты.
При создании студентов необходимо указать баллы за их следующие качества: courage (храбрость),
intelligence (интеллект), justice (справедливость), ambition (амбиции).
У студентов не могут быть качества одинакового уровня. В зависимости от того,
какое качество студента преобладает, метод sorting_hat будет распределять студента
в один из факультетов и выдавать в какой факультет поступил студент.
Примечание: 
Преобладает courage -> Gryffindor
Преобладает intelligence -> Ravenclaw
Преобладает justice -> Hufflepuff
Преобладает ambition -> Slytherin
"""
# писать код здесь
# class Hogwarts:
#     Gryffindor = 0
#     Ravenclaw = 0
#     Hufflepuff = 0
#     Slytherin = 0
#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition

#     def sorting_hat(self):
#         if (self.courage > self.intelligence and
#             self.courage > self.justice and
#             self.courage > self.ambition):
#             Hogwarts.Gryffindor += 1
#             return f'Преобладает courage -> Gryffindor'
            
#         elif  (self.intelligence > self.courage and
#                self.intelligence > self.justice and
#                self.intelligence > self.ambition):
#             Hogwarts.Ravenclaw += 1
#             return f'Преобладает intelligence -> Ravenclaw'

#         elif  (self.justice > self.intelligence and
#                self.justice > self.courage and
#                self.justice > self.ambition):
#             Hogwarts.Hufflepuff += 1
#             return f'Преобладает justice -> Hufflepuff'

#         elif  (self.ambition > self.intelligence and
#                self.ambition > self.justice and
#                self.ambition > self.courage):
#             Hogwarts.Slytherin += 1
#             return f'Преобладает ambition -> Slytherin'

# student1 = Hogwarts(12, 34, 65, 56)
# student2 = Hogwarts(78, 34, 32, 66)
# student3 = Hogwarts(65, 87, 65, 44)
# student4 = Hogwarts(78, 34, 65, 56)
# student5 = Hogwarts(60, 87, 50, 56)
# print(student1.sorting_hat())
# print(student2.sorting_hat())
# print(student3.sorting_hat())
# print(student4.sorting_hat())
# print(student5.sorting_hat())