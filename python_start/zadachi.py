"""
1) Создайте свой класс MyUser. В этом классе реализуйте следующие условия:
При инициализации объекта, необходимо передавать аргументы: name, last_name. Автоматически программа генерирует вам пароль password,
который состоит только из гласных букв, входящих в состав атрибутов name и last_name
При вызове самого объекта, возвращаются только первые буквы имени и фамилии, остальные буквы скрыты символом *
При попытке получения пароля (при вызове атрибута password) должна выдаваться ошибка-сообщение: “Forbidden”
	Например:
	user = MyUser(“Makers”, “Bootcamp”)
	print(user)  ->    M***** B*******
	print(user.password)  ->  Exception: Forbidden
"""
# class MyUser:
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.__password = [i for i in name if i.lower() in 'aeyuow']
#         [self.__password.append(i) for i in last_name if i.lower() in 'aeyuow']
#         self.__password = ''.join(self.__password)

#     @property
#     def password(self):
#         raise Exception('Foridden')

#     def __str__(self):
#         res = self.name[0] + '*'* len(self.name[1:]) + ' ' + self.last_name[0] + '*' * len(self.last_name[1:])
#         return res

# user = MyUser('Makers','Bootcamp')
# print(user)  
# # print(user.password)

"""
2) Создайте класс MyTuple. Создайте объекты от этого класса, они должны быть кортежами,
в которых элементы - числа. Далее сравните эти кортежи,
но сравнение должно происходить по сумме чисел в кортежах. Например:
a = (1,2,3,4,5)  - сумма 15
b = (6,7,8)        - сумма 21
print(a == b) -> False
print(a > b) -> False
print(a < b) -> True
print(a != b) -> True
"""
# class MyTuple(tuple):
#     def __init__(self, tuple_: tuple) -> None:
#         self.tuple = tuple_

#     def __str__(self):
#         return f'{self.tuple}'

#     def __gt__(self, other: str) -> bool:
#         return sum(self) > sum(other)

#     def __lt__(self, other: str) ->bool:
#         return sum(self) < sum(other)

#     def __eq__(self, other: str) -> bool:
#         return sum(self) == sum(other)

#     def __ne__(self, other: str) -> bool:
#         return sum(self) != sum(other)

# a = MyTuple((1,2,3,4,5))
# b = MyTuple((6,7,8))
# print(a)
# print(b)
# print(a == b)
# print(a > b)
# print(a < b)
# print(a != b)
# print(dir(a))

'''
Task association
1. Создайте абстрактный класс DaysAndDates с двумя методами: define_date и define_days. Создайте три дополнительных класса:
Current, MonthStart и MonthEnd. В Current необходимо вывести текущую дату. В MonthStart вывести первый день текущего месяца
и кол-во дней с первого дня до текущего дня. В MonthEnd вывести последний день текущего месяца и кол-во дней до конца месяца.
Даты выводить в формате: день/месяц/год, кол-во дней: в int.
К абстрактным методам добавить док-стринг с описанием методов.

2. Создайте абстрактный класс Car с методом get_info. Создайте класс Toyota и переопределите метод get_info так,
чтобы метод выводил информацию о типе автомобиля, пробеге и стоимости.

3. Создайте абстрактный класс Bank с атрибутами экземпляра класса name, interest_rate, term, loan_balance,
interest_balance и методами: get_product, loan_issue, interest_accrual и loan_repayment.
а) Создайте класс StartupLoan, переопределите метод get_product, чтобы он выводил информацию о кредитном продукте:
Кредитный продукт: “Стартап”
Процентная ставка: 20% годовых
Срок кредита: 2 года
b) Добавьте методы:
- loan_issue для выдачи кредита, который увеличивает сумму loan_balance и выводит сообщение “Кредит в сумме {сумма} сомов выдан {дата} года.”
- interest_accrual для начисления процентов со дня выдачи до конца месяца с выводом информации “Задолженность по процентам: {interest_balance} сомов”
- loan_repayment для погашения основной суммы и процентов с выводом информации: “Кредит погашен в сумме {сумма}.
Остаток по кредиту: {loan_balance} сомов, остаток по процентам: {interest_balance} сомов.”

К абстрактным методам добавить док-стринг с описанием методов.
'''
# from abc import abstractmethod, ABC
# from datetime import date

# class DaysAndDates(ABC):
# 	@abstractmethod
# 	def define_date(self):
# 		pass

# 	@abstractmethod
# 	def define_days(self):
# 		pass

# class Current(DaysAndDates):
# 	def define_date(self):
# 		date_now = date.today().strftime('%d/%m/%Y')
# 		print(f'Сегодняшняя дата: {date_now}')

# 	def define_days(self):
# 		pass

# class MonthStart(DaysAndDates):
# 	def define_date(self):
# 		Current.define_date()

# 	def define_days(self):
# 		first_day = date.today().strftime('01/%m/%Y')
# 		days = date.today() - date.resolution
# 		print(f'Первый день: {first_day}\nПрошло с первого дня: {days.day}')

# class MonthEnd(DaysAndDates):
# 	def define_date(self):
# 		Current.define_date

# 	def define_days(self):
# 		print(f'Последний день: {date.today().max.day}\nДней осталось до конца месяца: {date.today().max.day - date.today().day}')


# cur = Current()
# cur.define_date()

# month_start = MonthStart()
# month_start.define_days()

# month_end = MonthEnd()
# month_end.define_days()

# ------------------------------------

# from abc import ABC, abstractmethod

# class Car:
# 	@abstractmethod
# 	def get_info(self):
# 		pass

# class Toyota(Car):
# 	def __init__(self, type, prob, price) -> None:
# 		self.type = type
# 		self.prob = prob
# 		self.price = price

# 	def get_info(self):
# 		print(f'Тип Автомобиля Toyota: {self.type}\nПробег: {self.prob}\nЦена: {self.price}')

# car = Toyota('hybrid', 100, 2300)
# car.get_info()

# ------------------------------------

# from abc import abstractmethod, ABC
# from datetime import date

# class Bank(ABC):
# 	@abstractmethod
# 	def __init__(self, name, interest_rate, term, loan_balance, interest_balance) -> None:
# 		self.name = name
# 		self.rate = interest_rate
# 		self.term = term
# 		self.loan = loan_balance
# 		self.balanc = interest_balance

# 	@abstractmethod
# 	def get_product(self):
# 		pass

# 	@abstractmethod
# 	def loan_issue(self):
# 		pass

# 	@abstractmethod
# 	def interest_accrual(self):
# 		pass

# 	@abstractmethod
# 	def loan_repayment(self):
# 		pass

# class StartupLoan(Bank):
# 	def __init__(self, name, interest_rate, term, loan_balance, interest_balance) -> None:
# 		super().__init__(name, interest_rate, term, loan_balance, interest_balance)

# 	def get_product(self):
# 		return f'Кредитный продукт: {self.name}\nПроцентная ставка: {self.rate}\nСрок кредита: {self.term} года'

# 	def loan_issue(self, summa):
# 		from datetime import date
# 		self.loan += summa
# 		return f'Кредит в сумме {summa} сомов выдан {date.today().year} года.'

# 	def interest_accrual(self, percent):
# 		self.balanc += percent
# 		return f'Задолженность по процентам: {self.balanc} сомов'

# 	def loan_repayment(self, summa, percent):
# 		self.loan -= summa
# 		self.balanc -= percent
# 		return f'Кредит погашен в сумме {summa}. Остаток по кредиту: {self.loan} сомов, остаток по процентам: {self.balanc} сомов.'

# person = StartupLoan(name='start',
# 					interest_rate= 10,
# 					term= 7,
# 					loan_balance=15,
# 					interest_balance=2000)

# print(person.get_product())
# print(person.loan_issue(10000))
# print(person.interest_accrual(7))
# print(person.loan_repayment(summa=7000, percent=8))
