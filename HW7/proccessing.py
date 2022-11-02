import imp
from variable import *


id = 0
phone_book = []

def increase_id():
    """Увеличение id"""

    global id
    id += 1

def get_phone_book():
    if phone_book:
        return phone_book
    

def add_contact(contact):
    """Добавление контакта"""

    global phone_book
    phone_book.append(contact)


def create_contact(data):
    """Создание нового контакта"""

    contact = {}

    for key, value in zip(field_names, data):
        if key == field_names[0]:
            contact[key] = id

        contact[key] = value
    add_contact(contact)
    increase_id()

def new_contact():
    contact = {}

    contact[field_names[0]] = id
    for key in field_names[1:]:
        contact[key] = input(f'{key}: ')
    
    add_contact(contact)
    increase_id()


def import_contact():
    """импорт контакта"""

    file = input('Имя файла для импорта')
    with open(file, encoding='utf-8') as file:
        data = file.readlines()
        for line in data[1:]:
            create_contact(line.split())

# def export_contact():
#     """Экспорт контакта"""

#     if phone_book:
#         with open(export_file, 'w', encoding='utf-8') as file:
#             file.writeline(' '.join(field_names))
#             file.write('\n')
#             for contact in phone_book:
#                 file.writelines(' '.join)



