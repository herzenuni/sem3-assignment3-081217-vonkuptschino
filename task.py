

# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?

# Импортируйте необходимые библиотеки

# import 

# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных 
import pprint
import json

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        
        data = json.loads(data_file.read())

except FileExistsError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'

#pprint(data)

# Вывести в форматированном виде поля: 
# company, email, phone, address
for ix, i in enumerate(data):
    pp = {}
    pp.update(
        {'index': i.get('index'),
         'company': i.get('company'),
         'email': i.get('email'),
         'phone': i.get('phone'),
         'address':i.get('address')})
    pprint.pprint(pp)
