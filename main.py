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
def main(update:Update,context:CallbackContext):
    db=DB('db.json')
    bot=context.bot
    message_id=update.message.message_id
    chat_id=update.message.chat_id
    data=update.message.text

    if data=='Uzbekcha🇺🇿':
        db.add_lang('Uzbekcha🇺🇿',chat_id)
        bot.send_message(chat_id,'Asosiy menu')
        text="15-avftobusning siz uchun kerakli yo'nalishini tanlif lang\n\n*To'g'ri yo'nalish yo'nalish:\n📍Termiz Avtoshoxbekat ➡️ 📍Shimoliy Avtoshoxbekat (Yashil Dunyo)\n\n*Teskari yo'nalish: 📍Shimoliy Avtoshoxbekat (Yashil Dunyo) ➡️ 📍Termiz Avtoshoxbekat"
        btn=ReplyKeyboardMarkup([["To'g'ri yo'nalish🚌", "Teskari yo'nalish🚌"],['Avftobus yo\'nalishi haqida🗒']],resize_keyboard=True)
        bot.send_message(chat_id,text=text,reply_markup=btn)
    elif data == 'Русский🇷🇺':
        db.add_lang('Русский🇷🇺',chat_id)
        bot.send_message(chat_id,'Главное меню')
        text="Выберите нужное Вам направление 15-авфтобуса\n\n*Правильное направление:\n📍Термиз Автошохбекат ➡️ 📍Северный Автошохбекат (Яшил Дуне)\n\n*Обратное направление: 📍Северный Автошохбекат (Яшил Дуне) ➡️ 📍 Термез Автошохбекат"
        btn=ReplyKeyboardMarkup([["Правильное направление🚌", "Обратное направление🚌"],['Об автобусном маршруте🗒']],resize_keyboard=True)
        bot.send_message(chat_id,text=text,reply_markup=btn)
    db.save()


updater=Updater(token='')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,main))

updater.start_polling()
updater.idle()