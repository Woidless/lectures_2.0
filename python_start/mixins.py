'''
Задание 1
Создайте класс Auto в нем реализуйте метод ride
который выводит сообщение 'Riding on a ground'.
Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.
Создайте класс Amphibian который наследуется от класса Auto и Boat.
Создайте от него объект obj и вызовите все методы.
Ввод:
obj = Amphibian() 
obj.ride() 
obj.swim() 
Вывод:
Riding on a ground 
Floating on water 
'''

# class Auto: 
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 

'''
Задание 2
Создайте класс-миксин RadioMixin, и реализуйте в нем метод для проигрывания музыки play_music,
который принимает в переменную title название песни.
Метод должен печатать строку "Песня называется title",
где вместо title должно быть переданное название песни.
Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина.
Класс Amphibian также как в предыдущем задании должен наследоваться от классов Auto и Boat.
Создайте экземпляры auto, boat и obj от трех классов и примените метод play_music.
'''
# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian( Auto, Boat, RadioMixin):
#     pass

# auto, boat, obj = Auto(), Boat(), Amphibian()
# auto.play_music('sdf')
# boat.play_music('asdsd')
# obj.play_music('sdsdfsdf')
'''
Задание 3
Будильник. Создайте класс Clock, у которого будет метод current_time показывающий
текущее время и класс Alarm, с методами on и off для включения и выключения будильника.
Далее, создайте класс AlarmClock, который наследуется от двух предыдущих классов.
Добавьте к нему метод alarm_on для установки будильника, при вызове которого должен
включатся будильник.
Создайте экземпляр clock класса AlarmClock и примените к ниму методы current_time и alarm_on.
Ввод должен быть:
clock.current_time() 
clock.alarm_on() 
С выводом:
17:10:41 
Будильник включен 
'''
# class Clock:
#     def current_time(self):
#         import time
#         print(time.strftime('%H:%M:%S'))

# class Alarm:
#     def on(self):
#         pass

#     def off(self):
#         pass

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включен')

# clock = AlarmClock()

# clock.current_time() 
# clock.alarm_on() 
'''
Задание 4
Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и
абстрактными методами get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.
Класс Backend должен принимать дополнительно параметры experience и languages_backend,
а Frontend такие параметры как — experience и languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество
часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time.
Также бывают Fullstack разработчики, поэтому создайте данный класс так чтобы у него были
атрибуты и методы предыдущих классов. При этом нее определяйте никаких методов и атрибутов
в данном классе он должен наследовать их от родительских классов.
Создайте экземпляры a, b, c от классов Backend, Frontend, Fullstack соответственно и вызовите
их методы.
Ввод должен быть:
a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 
Вывод:
Python разработчик, уровень: Junior, потрачено 12 часов на программирование
Javascript разработчик, уровень: Middle, потрачено 45 часов на программирование
Python and JS разработчик, уровень: Senior, потрачено 17 часов на программирование 
'''
# from abc import ABC, abstractmethod
# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def coding(self):
#         pass

#     @abstractmethod
#     def get_info(self):
#         pass

# class Backend(Coder):
#     def __init__(self, experience, languages_backend) -> None:
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, hour):
#         self.count_code_time += hour

# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend) -> None:
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, hour):
#         self.count_code_time += hour

# class Fullstack(Backend, Frontend):
#     pass

# a = Backend('Middle', 'Python')
# b = Frontend('Junior', 'JavaScript')
# c = Fullstack('Senior', 'HTML')

# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info())
'''
Задание 5
Создайте два класса: Square и Triangle.
Класс Square должен иметь атрибуты: side - длина стороны квадрата.
Класс Triangle должен иметь аттрибуты: height - высота, base - длина.
У каждого из вышеуказанных классов должен быть метод get_area,
который высчитывает и возвращает площадь - результатом должно быть целое число.
Создайте третий класс Pyramid который наследуется от первых двух классов,
init унаследуйте от Triangle, дополнительные аттрибуты присваивать нельзя.
Добавьте метод get_volume для расчета объема пирамиды(формула: 1/3 x основание^2 x высоту),
метод должен возвращать целое число.
'''
# class Square:
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         return round(self.side*self.side)

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return (self.height * self.base) // 2

# class Pyramid(Triangle, Square):
#     def get_volume(self):
#         return int(1/3 * self.base**2 * self.height)

# square = Square(5)
# triangle = Triangle(5, 3)
# pyramid = Pyramid(5, 6)
# print(square.get_area())
# print(triangle.get_area())
# print(pyramid.get_area())
'''
Задание 6
Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.
У класса должен быть один метод set_deadline, который принимает дату дедлайна
(в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.
Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:
в классе CreateMixin определите метод create, который принимет в
себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos,
если ключ уже существует верните "Задача под таким ключём уже существует".
класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key,
который передается как аргумент, и возвращает сообщение 'удалили название задачу',
где вместо слова название должно быть название задачи.
класс UpdateMixin должен содержать метод update, который принимает в себя ключ
key и новое значение new_value и заменяет задачу под данным ключом на новое значение.
класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
'''
# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():    
#             return 'Задача под таким ключём уже существует'
#         self.todos[key] = todo 
#         return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_: return delete_
#         return delete_

# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos
        
# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         import datetime
#         # time_ = datetime.datetime.now().strftime('%d/%m/%Y')

#         deadline = deadline.split('/')
#         # time_ = time_.split('/')
        
#         deadline = list(map(int, deadline))
#         # time_ = list(map(int, time_))

#         # time_ = sum((time_[0], time_[1]*30, time_[2]*365))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
        
#         return (deadline - time_).days

# task = ToDo()
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# -------------
# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():    
#             return 'Задача под таким ключём уже существует'
#         self.todos[key] = todo 
#         return self.todos
            

# class DeleteMixin:
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_: return delete_
#         return delete_

# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos
        
# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    
#     def __init__(self):
#         self.todos = {}
        
#     def set_deadline(self, deadline):
#         import datetime
#         # time_ = datetime.datetime.now().strftime('%d/%m/%Y')

#         deadline = deadline.split('/')
#         # time_ = time_.split('/')
        
#         deadline = list(map(int, deadline))
#         # time_ = list(map(int, time_))

#         # time_ = sum((time_[0], time_[1]*30, time_[2]*365))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
        
#         return (deadline - time_).days

# task = ToDo()
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1,  'todo'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('6/7/2022'))
'''
Задание 7
Напишите класс Game, с помощью которого можно создать объекты-игры,
у объектов должны быть атрибуты:
type - тип игры
name - название игры,
extensions соответсвующий пустому списку - [].
У класса должны быть методы:
get_description, который принимает строку и возвращает описание к игре в виде названия игры и переданной строки:
Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром. 
Где Minecraft - это название игры, берется из атрибута name объекта.
get_extensions, который возвращает все подключенные расширения в виде строки разделенной пробелами,
если же список extensions пуст, возвращайте сообщение:
Нет подключенных расширений   
Также напишите миксин ExtensionMixin, чтобы к игре можно было подключать расширения.
У миксина должно быть два метода:
add_extension, принимающий строку-название и добавляющий ее в список игры, также должен возвратить сообщение:
Добавлено новое расширение Multiverse-Core для игры Minecraft. 
где Multiverse-Core это строка - название расширения
remove_extension, удаляющий расширение по названию, и возращающий строку в формате:
Multiverse-Core был отключен от Minecraft. 
Если же такого расширения нет в списке должна возвращаться строка:
Такого расширения нет в списке.
'''

# class ExtensionMixin:
#     def add_extension(self, extension):
#         self.extensions.append(extension)
#         return f'Добавлено новое расширение {extension} для игры {self.name}'

#     def remove_extension(self, extension):
#         if extension in self.extensions:
#             delete = self.extensions.pop(self.extensions.index(extension))
#             return f'{delete} был отключен от {self.name}'
#         return 'Такого расширения нет в списке.'

# class Game(ExtensionMixin):
#     def __init__(self, type, name, ) -> None:
#         self.type = type
#         self.name = name
#         self.extensions = []
    
#     def get_description(self, description):
#         return f'{self.name} это {description}'

#     def get_extensions(self):
#         if not self.extensions:
#             return 'Нет подключенных расширений'
#         return ' '.join(self.extensions)

# obj = Game(10, 'Minecraft')
# print(obj.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром.'))
# print(obj.add_extension('Multiverse-Core'))
# print(obj.remove_extension('Multiverse-Core'))
# print(obj.get_extensions())
'''
Таск 8
Создайте класс WalkMixin с методом walk, который будет выводить "я могу ходить"
Создайте класс FlyMixin с методом fly, который будет выводить "я могу летать"
Создайте класс SwimMixin с методом swim, который будет выводить "я могу плавать"
Создайте класс Human, который будет наследоваться от миксинов WalkMixin и SwimMixin
Создайте класс Fish, который будет наследоваться от миксина SwimMixin
Создайте класс Exocoetidae, который будет наследоваться от миксинов FlyMixin и SwimMixin
Создайте класс Duck, который будет наследоваться от всех 3 миксинов
Создайте обьекты от классов Human, Fish, Exocoetidae, Duck и вызовите методы,
которые у них есть от миксинов
'''
# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')

# class FlyMixin:
#     def fly(self):
#         print('я могу летать')

# class SwimMixin:
#     def swim(self):
#         print('я могу плавать')

# class Human(WalkMixin, SwimMixin):
#     pass

# class Fish(SwimMixin):
#     pass

# class Exocoetidae(FlyMixin, SwimMixin):
#     pass

# class Duck(WalkMixin, FlyMixin, SwimMixin):
#     pass

# human = Human()
# fish = Fish()
# exo = Exocoetidae()
# duck = Duck()
# human.walk()
# human.swim()
# fish.swim()
# exo.fly()
# exo.swim()
# duck.walk()
# duck.fly
# duck.swim()