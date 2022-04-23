# S = 'Hello'
#
# print(f'This is {S}')
# S_encoded = S.encode('utf-8')
#
# print(f'Encoded version is {S_encoded}')
#
# print(S_encoded.decode('utf-8'))

# with open('readme.txt', 'r') as f:
#     print(f.read())


import json

# data = {
#     'Belarus': 'Minsk',
#     'Germany': 'Berlin',
#     'Poland': 'Warszawa'
# }
# with open('file.json', 'w') as file:
#     json.dump(data, file)
# with open('file.json', 'r') as file:
#     data = json.load(file)
#     print(data)
#     print(type(data))
#     print(f'Столица Беларуси - {data["Belarus"]}')

# import csv
#
# with open('test.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=['Name', 'Profession', 'Age'])
#     writer.writeheader()
#     writer.writerow({"Name": "Ivan", "Profession": "Taxi", "Age": 50 })

# a = b'r\xc3\xa9sum\xc3\xa9'
# b = a.decode('UTF-8')
# b_2 = b.encode('Latin1')
# print(b_2.decode('Latin1'))
# a = input("Введите первую строку: ")
# b = input('Введите вторую строку: ')
# c = input('Введите третью строку: ')
# d = input("Введите четвертую строку: ")
# file = open('example_4.txt', 'w')
# file.write(a)
# file.write('\n')
# file.write(b)
# file.write('\n')
# file.close()
# file = open('example_4.txt', 'a')
# file.write(c)
# file.write('\n')
# file.write(d)


dict = {
    1213124: ('Slava', '45'),
    4564756: ('Sergey', '66'),
    3465467: ('Daniil', '33')
}
# with open('www.json', 'w') as file:
#     json.dump(dict, file)


def decorator_fucntion(func):
    def wrapper(dict):
        func(dict)
        print(f"ID-номер функции function_2: {id(func)}")
    return wrapper


@decorator_fucntion
def function_2(dict):
    file = input("Введите название файла: ") + '.json'
    with open(file, 'a+') as f:
        json.dump(dict, f)


function_2(dict)

# with open('urok.json', 'w') as file:
#     json.dump(dict, file)
# import csv
# with open('urok.json', 'r') as file:
#     data = json.load(file)
#
# with open('urok2.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Number'])
#     writer.writeheader()
#     writer.writerows(data.values)