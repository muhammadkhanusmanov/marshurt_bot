from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from db import DB




def start(update:Update,context:CallbackContext):
    db=DB('db.json')
    bot=context.bot
    chat_id=update.message.chat_id
    db.starting(chat_id)
    db.save()
    first_name=update.message.from_user.first_name
    bot.sendMessage(chat_id,f'Assalomu alaykum {first_name}\n_____________\nздравствуйте {first_name}')
    text='Tilni tanlang\n_____________\nВыберите язык'
    btn=ReplyKeyboardMarkup([['Uzbekcha🇺🇿','Русский🇷🇺']],resize_keyboard=True)
    bot.sendMessage(chat_id,text=text,reply_markup=btn)

updater=Updater(token='')
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()