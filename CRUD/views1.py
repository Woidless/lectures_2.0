import json
from wsgiref.util import request_uri

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def get_one_data():
    data = get_data()
    id = int(input('Введите id продукта: '))
    element = list(filter(lambda x: x['id'] == id, data))[0]
    return element

def post_data():
    data = get_data()
    data.append({
        'id': int(input('Введите ID продукта(1-100): ')),
        'name': input('Введите название продукта: '),
        'price': float(input('Введите стоимость продукта: '))
    })

    with open(FILE_PATH, 'w+') as file:
        json.dump(data, file)
    return 'CREATED'

def update_data():
    data = get_data()
    id = int(input('Введите ID продукта: '))
    # choice_ = input(f'Что хотите изменить в товаре {data[id]}')
    update = list(filter(lambda x: x['id'] == id, data))[0]

    if not update: return 'Нет такого продукта'

    index_ = data.index(update)
    data[index_]['name'] = input('Введите новое назвние продукта: ')
    data[index_]['price'] = input('Введите новую стоимость продукта: ')
    
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

def delete_data():
    data = get_data()
    id = int(input('Введите ID продукта: '))
    delete = list(filter(lambda x: x['id'] == id, data))[0]
    
    if not delete: return 'Нет продукта с таким индексом'

    index_ = data.index(delete)
    data.pop(index_)

    json.dump(data, open(FILE_PATH, 'w'))
    return 'DELETED'