yes_or_no = True
while yes_or_no:

    x = input('Введите первое число: ')
    y = input('Введите второе число: ')

    if not x.isdigit() or not y.isdigit():
        print('Пожалуйста, введите целые числа')
        continue

    x = int(x)
    y = int(y)
    
    print('''Введите операцию: 
    "+" -- сложение
    "-" -- вычитание
    "/" -- деление
    "*" -- умножение
    "//" -- деление только целой части
    "%" -- остаток от деления''')
    
    mark = input('Операция: ')
    if mark == '+':
        print(f'{x} + {y} == {x + y}' )
    elif mark == '-':
        print(f'{x} - {y} == {x - y}' ) 
    elif mark == '/':
        if y == 0:
            print('На ноль делить нельзя')
        else:
            print(f'{x} / {y} == {x / y}' )
    elif mark == '*':
        print(f'{x} * {y} == {x * y}' ) 
    elif mark == '//':
        if y == 0:
            print('На ноль делить нельзя')
        else:
            print(f'{x} // {y} == {x // y}' )
    elif mark == '%':
        if y == 0:
            print('На ноль делить нельзя')
        else:
            print(f'{x} % {y} == {x % y}' )
    else:
        print('Такой операции нет')
    
    while True:
        yon = input('Хотите продолжить работу? (y/n): ')
        if yon == 'n' or yon == 'N' :
            yes_or_no = False
            break
        elif yon == 'y' or yon == 'Y':
            print('Продолжаем)')
            break
        else:
            ('Выберите указанные варианты: (y/n)')
print('Работа завершена')