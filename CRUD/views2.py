import json

FILE_PATH = 'data.json'

# def custom_get_gata(func):
#     def wapper():
#         [print(func()[i]) for i in range(len(func()))]
#     return wapper
# @custom_get_gata

def get_data():
    
    with open(FILE_PATH) as file:
        return json.load(file)

def show_data():
    [print(get_data()[i]) for i in range(len(get_data()))]
    return 'Список товаров'

def get_one_product():
    data = get_data()
    id_ = input()
    product = list(filter(lambda x: x['id'] == id, data))[0]
    if product: return product
    else : return 'Такого продукта нет'

def get_id():
    with open('id.txt', 'r') as file:
        id_ = int(file.read())
        id_ += 1
    with open('id.txt', 'w')as file:
        file.write(str(id_))
    return id_

def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'title' : input('Введите название продукта: '),
        'price': float(input('введите цену: '))
    }
    data.append(product)
    with open(FILE_PATH, 'w')as file:
        json.dump(data, file)
    return 'CREATED'

def update_product():
    data = get_data()
    flag = False
    id_ = int(input('Введите айди: '))
    product = list(filter(lambda x: x['id'] == id_, data))[0]

    if not product: return 'Такого продукта нет'
    
    index_ = data.index(product)
    print(data[index_])
    print('-'*50)
    print(data[index_]['title'])
    print('-'*50)
    print(data[index_]['price'])
    print('-'*50)
    choice_ = input('Что вы хотите изменить?\n(1 - title)\t(2 - price): ')

    if choice_ == '1':
        data[index_]['title'] = input('Введите новое название: ')
        flag = True
    elif choice_ == '2':
        data[index_]['price'] = input('Введите новую сумму: ')
        flag = True
    else: print('Нет такой команды')

    with open(FILE_PATH, 'w')as file:
        json.dump(data, file)

    if flag: return 'UPDATED'
    else: return 'NOT UPDATED'

def delete_product():
    data = get_data()
    id_ = int(input('Введите ID: '))
    product = list(filter(lambda x: x['id'] == id_, data))[0]

    if not product: return 'Нет такого продукта'
    
    index_ = data.index(product)

    data.pop(index_)

    json.dump(data, open(FILE_PATH, 'w'))

    return 'DELETED'