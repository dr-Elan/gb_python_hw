from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


updater = Updater('5474829142:AAHkUsF0d-9tHTPi1vnfWyct91r94XnajfY')


updater.dispather.add_handler(CommandHandler('menu', menu_command))
updater.dispather.add_handler(CommandHandler('sum_poly', sum_poly_command))

print('server run')
updater.start_polling()
updater.idle()


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5474829142:AAHkUsF0d-9tHTPi1vnfWyct91r94XnajfY").build()
# print('server run')
# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()