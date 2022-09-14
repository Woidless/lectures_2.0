"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm,
с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""
# class Clock:
#     def now(self):
#         from datetime import date
#         print(date.strftime('%H:%M:%S'))

# class Alarm:
#     def on(self):
#         print('Будильник включен')

#     def off(self):
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     def ustanovka(self):
#         super().on()

# obj = AlarmClock()
# obj.now()


"""
2) Напишите класс Student, который описывает студента. У студента есть следующие атрибуты:
имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""
# def decor_sr(func):
#     def wrapper(self, other):
#         self = sum(self.ball.values()) / len(self.ball.values())
#         other = sum(other.ball.values()) / len(other.ball.values())
#         return func(self, other)
#     return wrapper

# class Student:
#     def __init__(self, name, last_name, class_, ball) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.class_ = class_
#         self.ball = ball

#     @decor_sr
#     def __eq__(self, other):
#         return self == other

#     @decor_sr
#     def __gt__(self, other):
#         return self > other

#     @decor_sr
#     def __ge__(self, other):
#         return self >= other
    
#     @decor_sr
#     def __lt__(self, other):
#         return self < other
    
#     @decor_sr
#     def __le__(self, other):
#         return self <= other

# student1 = Student('No', 'One', 'B', {'math': 100, 'history': 89,'literature': 88})
# student2 = Student('Any', 'One', 'S', {'math': 90, 'history': 80,'literature': 70})

# print(student1 == student2)
# print(student1 > student2)
# print(student1 < student2)
# print(student1 >= student2)
# print(student1 <= student2)
"""
3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 
- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)
Также класс должен содержать следующие методы:
- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""
# class Makers:
#     students_count = 0
#     def __init__(self, name,  language) -> None:
#         self.name = name
#         self.lang = language
#         Makers.students_count += 1

#     def info(self):
#         return f'name: {self.name}, language: {self.lang}'

#     def get_kpi(self, kpi):
#         self.kpi = kpi
#         return self.kpi

# stud_maker1 = Makers('Azamat', 'English')
# print(stud_maker1.info())
# print(stud_maker1.get_kpi(100))
# print(stud_maker1.kpi)

# stud_maker2 = Makers('Aitaliev', 'French')
# print(stud_maker2.info())
# print(stud_maker2.get_kpi(90))
# print(stud_maker2.kpi)

# stud_maker3 = Makers('Bruno', 'Italian')
# print(stud_maker3.info())
# print(stud_maker3.get_kpi(98))
# print(stud_maker3.kpi)

# print(f'Количестко студентов: {Makers.students_count}')

"""
4) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:
dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"
Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()
//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

# def dollarize(self, float_: float):
    
#     return f'{''}'

# class MoneyFmt:
#     def __init__(self, amount) -> None:
#         self.amount = amount

#     def update(self):
#         pass

#     def __repr__(self) -> str:

#         return round(self, 1)

#     def __str__(self) -> str:
#         return dollarize(self.amount)



"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram.
При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона,
который должен быть int. При регистрации в Telegram необходимо передавать номер телефона и username.
Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку
“I am sending a text ...” и вместо … должен быть сам текст сообщения. В SnapChat send принимает
image и text, при этом image должен быть булевым типом данных. Если image True, то выдается сообщение
“I am sending a text … with some image ”, если  False - сообщение “I am sending a text … without image”.
В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a
voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""
# писать код здесь
# class WhatsApp:
#     def __init__(self, number: int) -> None:
#         self.number = number

#     def send(self, text):
#         return f'I am sending a text {text}'

# class SnapChat:
#     def __init__(self, number: int) -> None:
#         self.number = number

#     def send(self, image, text):
#         if image: return f'I am sending a text {text} with some image'
#         else: return f'I am sending a text {text} without image'

# class Telegram:
#     def __init__(self, number: int, name: str) -> None:
#         self.number = number
#         self.name = name

#     def send(self, voice_message):
#         return f'I am sending a voice message {voice_message}'

# wp = WhatsApp(996777777777)
# sc = SnapChat(996888888888)
# tg = Telegram(996996996996, 'Cool')
# print(wp.send('IM STRONGER! IM SMARTER! IM BETTER!'))
# print(sc.send(text='NICE', image=True))
# print(sc.send(text='NICE', image=False))
# print(tg.send('MosHy Moshy'))

"""
2) Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает,
сколько гласных букв в слове, которое передается в качестве аргумента в методе count,
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и
вызовите этот метод у каждого объекта.
"""
# писать код здесь
# class A:
#     def count(self, string):
#         return sum([1 for i in string if i in 'weyiua'])

# class B:
#     def count(self, string):
#         return sum([1 for i in string if i in 'qrtpsdfghjklzxcvbnm'])

# a = A()
# print(a.count('eeerrreee eeerrreee'))

# b = B()
# print(b.count('eeerrreee aeyrrr'))

