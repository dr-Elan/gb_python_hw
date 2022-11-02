from proccessing import *
from UI import *


def run():
    """Запуск программы"""

    greetings()
    running = True
    while running:
        show_menu()
        action = input('Ответ: ')
        if action == '1':
            show_phone_book(get_phone_book())

        elif action == '2':
            insert()
            new_contact()
            contact_added()
        elif action == '3':
            import_contact()
            succes_import()
        else:
            show_error()

    bay()
