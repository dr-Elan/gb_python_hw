import fractions
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import sympy
import re

def menu_command(update: Update, context: CallbackContext):
    update.message.reply_text('введите через / выбраннаую функцию: ')
    update.message.reply_text(f'сумма многочлена \n /sum_poly\n')

def sum_poly_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    poly1 = sympy.polys.polytools.poly_from_expr(str(items[1]))[0]
    poly2 = sympy.polys.polytools.poly_from_expr(str(items[1]))[1]
    print(poly1)
    print(poly2)
    polysum = poly1 + poly2
    a = str(polysum.as_expr()).replace('**', '^')+ ' = 0'
    update.message.reply_text(f'{a}')
    



