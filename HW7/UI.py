from tabulate import tabulate
from variable import *

def init():
    global phone_book, contact, field_names, expor_file, id

def greetings():
    '''приветсвие'''

    line = 'Здравствуйте. Вас приветсвует программа "Телефонный справочник"'
    decor = len(line) * '-'
    print(decor, line, decor, sep = '\n', end='\n\n')

def show_menu():
    """Меню"""

    print(menu)

def show_error():
    line = 'произошла ошибка, проверьте данные'
    decor = len(line)* '-'
    print(decor, line, decor, sep='\n', end='\n\n')

def insert():
    line = 'Введите данные'
    decor = len(line)* '-'
    print(decor, line, decor, sep='\n', end='\n\n')
    
def contact_added():
    line = 'Контакт добавлен'
    decor = len(line)* '-'
    print(decor, line, decor, sep='\n', end='\n\n')

def success_export():
    line = f'Данные экспортированы в файл {export_file}'
    decor = len(line)* '-'
    print(decor, line, decor, sep='\n', end='\n\n')

def succes_import():
    line = 'Данные импортированы!'
    decor = len(line)* '-'
    print(decor, line, decor, sep='\n', end='\n\n')

def show_phone_book(phone_book):
    if phone_book:
        print(
            tabulate(
                phone_book, 
                headers='keys'
            ), end='\n\n'
        )
    else:
        show_error()

def bay():
    line = 'До скорой встречи!'

    decor = len(line)* '-'
    print(decor, line, decor, sep='\n', end='\n\n')




