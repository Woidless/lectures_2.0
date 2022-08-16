'''  
C - create
R - retrieve
U - update
D - delete

'''

id_ = 4
data = [
        {'id': 1,
        'title': 'Redmi Note 10',
        'price': 250,
        'description': 'gold phone'},
        {'id': 2,
        'title': 'Redmi Note 9',
        'price': 150,
        'description': 'green phone'},
        {'id': 3,
        'title': 'iPhine 10',
        'price': 350,
        'description': 'silver phone'},
        {'id': 4,
        'title': 'Poco F4',
        'price': 250,
        'description': 'grey phone'},
]

def create_product():
    '''
    add object in data
    '''
    prod = {
           'id': get_id(),
           'title': input('Продукт: '),
           'price': float(input('Price: '))
    }
    data.append(prod)
    
def list_of_prods():
    '''
    show list of data
    '''
    for prods in data:
        for k, v in prods.items():
            print(f'{k} : {v}')
        print()

def detail_retrieve():
    '''
    show element from data
    '''
    global data
    id_prod = int(input('input ID: '))
    try:
        prod = list(filter(lambda x: x['id'] == id_prod, data))[0]
    except IndexError:
        print('Такого индекса нет')
    else:
        print(prod)

def get_id():
    '''
    incremation
    '''
    id_ = data[-1]
    id_ += 1
    return id_

def update_prod():
    '''
    change element from data
    '''
    id_prod = int(input('ID: '))
    flag = False

    try: 
        prod = list(filter(lambda x: x['id'] == id_prod, data))[0]
    except:
        print('Нет индекса')
    else:
        index_ = data.index((prod))
        choice_ = input('''What changed?\n1 - title, 2 - price, 3 - desc\ninput: ''')

        if choice_ == '1':
            data[index_]['title'] = input('change title: ')
            flag == True
        elif choice_ == '2':
            data[index_]['price'] = input('change price: ')
            flag == True
        elif choice_ == '3':
            data[index_]['description'] = input('change description: ')
            flag == True
        else: 
            print('Error Index')

    if flag:
        print('Updated)))')    
    else:
        print('Not uptade')


def delete_prod():
    '''
    delete element from data
    '''
    id_prod = int(input('ID: '))
    flag = False
    try: 
        prod = list(filter(lambda x: x['id'] == id_prod, data))[0]
    except:
        print('Нет индекса')
    else:
        index_ = data.index(prod)
        data.pop(index_)
        flag = True
    
    if flag:
        print('Deleted!\n')
    else:
        print('not deleted\n')