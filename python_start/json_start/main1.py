'''JSON'''
'''
Задание 1
Вам даны два файла task1.json и task1.py.
В task1.json хранятся определенные данные, вам нужно прочитать данный файл,
затем сохранить содержимое в переменной python_obj.
После, откройте файл task1.py и запишите туда содержимое переменной python_obj.
'''
# import json task1.json  
# with open('task1.json', 'r') as file_: 
#     python_obj = json.load(file_) 
#     with open('task1.py', 'w') as file_inner: 
#         file_inner.write(str(python_obj))
'''
Задание 2
В task2.json хранятся данные в формате JSON.
Напишите программу Python которая будет считывать данные с файла и сохранять их в переменной json_obj.
Затем, преобразуйте это обьект в объект Python и запишите результат в переменную python_obj.
'''
# import json 
# with open('task2.json') as file_: 
#     json_obj = file_.read()
#     python_obj = json.loads(json_obj) 
'''
Вам дан объект Python сохраненный в переменной python_obj и имеющий значение None.
Преобразуйте данный объект в формат JSON и сохраните в переменной json_obj.
'''
# import json 
# python_obj = None
# json_obj = json.dumps(python_obj)
# print(json_obj)
'''
Задание 4
В переменной json_obj сохраните JSON объект "null",
затем преобразуйте данный JSON объект в объект Python и сохраните в переменной python_obj.
 После распечатайте содержимое переменной python_obj.
'''
# import json
# json_obj = "null"
# python_obj = json.loads(json_obj)
# print(python_obj)