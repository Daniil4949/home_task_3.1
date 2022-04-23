# def work_with_file():
#     name_file = input('Введите название файла: ')
#     fact = True
#     while fact:
#         print('1 - Создание файла и запись информации в него\n')
#         print('2 - Чтение файла\n')
#         print('3 - Очистка файла\n')
#         print('4 - Выход из программы\n')
#         choise = int(input('Введите значение: '))
#         if choise == 1:
#             create_file(name_file)
#         elif choise == 2:
#             read_file(name_file)
#         elif choise == 3:
#             clear_file(name_file)
#         elif choise == 4:
#             fact = False
#         else:
#             print('Неверно введенное значение!')
#             continue
#
#
# def create_file(name_file):
#     with open(name_file+'.txt', 'w') as file:
#         info = input('Введите информацию, которую вы хотите записать в файл: ')
#         file.write(info)
#
#
# def read_file(name_file):
#     with open(name_file+'.txt', 'r') as file:
#         info = file.readlines()
#         print(info)
#
#
# def clear_file(name_file):
#     file = open(name_file+'.txt', 'w').close()
#
#
# work_with_file()
# import csv
# import random
#
#
# def main():
#     n = int(input(('Введите количество элементов исходного массива:\n')))
#     arr = []
#     for i in range(n):
#         i = random.randint(1, 100)
#         arr.append(i)
#
#     array_1 = list(filter(lambda x: x % 2 == 0, arr))
#     array_2 = list(filter(lambda x: x % 2 != 0, arr))
#
#     with open('urok_3.csv', 'w') as file:
#         writer = csv.DictWriter(file, fieldnames=['Even numbers', 'Odd numbers'])
#         writer.writeheader()
#         writer.writerow({'Even numbers': array_1, 'Odd numbers': array_2})
#
#
# main()
# import json
# import csv
#
#
# def main():
#     data = {
#         'Slava': ['47', 'Minsk'],
#         'Oleg': ['34', 'Berlin'],
#         'Sergey': ['25', 'Paris']
#     }
#     with open('file.json', 'w') as file:
#         json.dump(data, file)
#     with open('file.json', 'r') as file:
#         result = json.load(file)
#     i = 1
#     for value in data.values():
#         value = value.append(str(i))
#         i += 1
#     with open('file_7.csv', 'w') as file:
#         writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City', 'Number'])
#         info = data.values()
#         names = list(data.keys())
#         writer.writeheader()
#         info = list(info)
#         for i in range(len(names)):
#             writer.writerow({'Name': names[i], 'Age': info[i][0], 'City': info[i][1], 'Number': info[i][2]})
#
#
# main()

# import random
# import csv
#
# A = [random.randint(1,10) for i in range(20)]
# file = open('numbers.csv', 'w', encoding='UTF-8')
# writer = csv.DictWriter(file, fieldnames=['Четные', 'Нечетные'])
# writer.writeheader()
#
# even = []
# odd = []
#
# for i in A:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# #print(len(even))
# #print(len(odd))
#
# for i in range(len(even) if len(even) < len(odd) else len(odd)):
#     writer.writerow({'Четные': even[i], 'Нечетные': odd[i]})
#
# file.close()

import re


def isfloat(s):
    find = re.fullmatch(r"\d*\.\d+", s)
    if find:
        return True
    else:
        return False


def check(s):
    fact = False
    pattern = r'[0-9]'
    for i in s:
        if re.search(pattern, i):
            fact = True
        else:
            return False
    return fact


def check_str(s: str):
    if isfloat(s) or check(s) or (check(s[1:]) and s[0] == '-') or (isfloat(s[1:]) and s[0] == '-'):
        if s.isdigit():
            print(f'Вы ввели положительное целое число: {s}')
            result = int(s)
        elif s[1::].isdigit() and s[0] == '-':
            print(f'Вы ввели отрицательное целое число: {s}')
            result = int(s)
            result *= -1

        elif isfloat(s[1:]) and s[0] == '-':
            print(f'Вы ввели дробное отрицательное число: {s}')
            result = float(s[1:])
            result *= -1
        elif isfloat(s) == True:
            result = float(s)
            print(f'Вы ввели дробное положительное число: {s}')
            return result

    else:
        print(f'Вы ввели некорректное число: {s}')
        return -1


check_str('55')
check_str('-55')
check_str('55.1')
check_str('.1')
check_str('-.11')
check_str('-55.1')
check_str('3grvfd')