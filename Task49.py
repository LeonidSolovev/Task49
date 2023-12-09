# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError('Невалидно Имя!')
            else:
               is_valid_name = True 
        except NameError as err:
            print(err)
            continue
        
    is_valid_name = False
    while not is_valid_name:
        try:
            last_name = input("Введите Фамилию: ")
            if len(last_name) < 2:
                raise NameError('Невалидна Фамилия!')
            else:
               is_valid_name = True 
        except NameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверна длина номера!')
            else:
                is_valid_phone = True
        except ValueError:
            print('Не валидный номер!')
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for elem in res:
        if elem["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def line_copy(file_name):
    count = 0 
    res = []
    c = int(input("Какую строку скопировать? "))+1
    with open(file_name, "r", encoding='utf-8') as data:
        for line in data:
            count +=1
            if count == c:
                print(line)
            res = list(line.split(','))
            print(res)
            write_file('phone1.csv', res)
                # co = 0
                # for el in line:
                #     res.append(line[co]) 
                #     co += 1
                #     print(res)
                # print(res.append(line.split(',')))
            # write_file(choose_file(), res)

def choose_file():
    file_name = 'phone.csv'
    file1_name = 'phone1.csv'

    file = int(input('Введите номер файла: '))
    if file == 1:
        return file_name
    elif file == 2:
        return file1_name
    else:
        print('Такого файла не существует')


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            a = choose_file()
            if not exists(a):
                create_file(a)
            write_file(a, get_info())
        elif command == 'r':
            a = choose_file()
            if not exists(a):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(a))
        elif command == 'lc':
            a = choose_file()
            line_copy(a)
            

main()