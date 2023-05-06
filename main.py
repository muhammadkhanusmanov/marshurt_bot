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
    
    elif data == 'Avftobus yo\'nalishi haqida🗒':
        text = "15-avftobus yo'nalishi chizmasi(xaritasi)"
        # photo =  ''
        # bot.send_photo(chat_id,photo=photo,caption=text)
        text="""
        15 - avftobus yo'nalishidagi to'xtash bekatlari
        ________________________________

        Termiz Avtoshoxbekat:
        <a href='https://goo.gl/maps/H9sr9n5cVaTJfm3bA'>📍Joylashuv</a>
        ___________________
        2-Akademik litsey bekati
        <a href='https://goo.gl/maps/jgnF7LraX3fWWsq6A'>📍Joylashuv</a>
        ___________________
        Hakim Termiziy masjidi bekati
        <a href='https://goo.gl/maps/S59WraEs4nc3VsNm8'>📍Joylashuv</a>
        ___________________
        Mashhura klinikasi bekati 
        <a href='https://goo.gl/maps/mVKHjLt3aLXfAY8F9'>📍Joylashuv</a>
        ___________________
        Hakim Termiziy masjidi bekati
        <a href='https://goo.gl/maps/S59WraEs4nc3VsNm8'>📍Joylashuv</a>
        ___________________
        Ankalogiya shifoxonasi bekati
        <a href='https://goo.gl/maps/SxDyBkYrb1DoywgM8'>📍Joylashuv</a>
        ___________________
        Temir yo'l bekati
        <a href='https://goo.gl/maps/mpEqdhR5sdkJVSgbA'>📍Joylashuv</a>
        ___________________
        Prezident maktabi bekati
        <a href='https://goo.gl/maps/b1BBmSXfzqCdAmuNA'>📍Joylashuv</a>
        ___________________
        Yubleniy bekati
        <a href='https://goo.gl/maps/VXXQipsYtiGsfHR48'>📍Joylashuv</a>
        ___________________
        Barkamol avlod bekati
        <a href='https://goo.gl/maps/SPNRdz1Z8g4AcbQ89'>📍Joylashuv</a>
        ___________________
        TERDU bekati
        <a href='https://goo.gl/maps/eneVkAdyr3AvKGgJ9'>📍Joylashuv</a>
        ___________________
        Istiqlol bekati
        <a href='https://goo.gl/maps/jLgQPMZGkvo1tAnx7'>📍Joylashuv</a>
        ___________________
        Surxon stadioni bekati
        <a href='https://goo.gl/maps/J7DTDbmbtmbL1SnN9'>📍Joylashuv</a>
        ___________________
        Surxon stadioni bekati
        <a href='https://goo.gl/maps/J7DTDbmbtmbL1SnN9'>📍Joylashuv</a>
        ___________________
        Olimpiada zaxiralar kolleji bekati
        <a href='https://goo.gl/maps/Gw7U6feQUQkmYSYn7'>📍Joylashuv</a>
        ___________________
        Shimoliy Avtoshoxbekati (Yashil Dunyo)
        <a href='https://goo.gl/maps/c6rmMwhsSCVwCmqv9'>📍Joylashuv</a>
        ___________________
        """
        bot.send_message(chat_id,text,parse_mode='HTML')
    elif data=='Об автобусном маршруте🗒':
        text="""
        15 - автобусные остановки
        ________________________________

        Термез Автошохбекат:
        <a href='https://goo.gl/maps/H9sr9n5cVaTJfm3bA'>📍Местоположение</a>
        ___________________
        2-Академический лицей остановка
        <a href='https://goo.gl/maps/jgnF7LraX3fWWsq6A'>📍Местоположение</a>
        ___________________
        Мечеть Хакима Термизи, остановка
        <a href='https://goo.gl/maps/S59WraEs4nc3VsNm8'>📍Местоположение</a>
        ___________________
        клиника Машхура
        <a href='https://goo.gl/maps/mVKHjLt3aLXfAY8F9'>📍Местоположение</a>
        ___________________
        Мечеть Хакима Термизи, остановка
        <a href='https://goo.gl/maps/S59WraEs4nc3VsNm8'>📍Местоположение</a>
        ___________________
        Oнкологической больницы остановка
        <a href='https://goo.gl/maps/SxDyBkYrb1DoywgM8'>📍Местоположение</a>
        ___________________
        Железнодорожная остановка
        <a href='https://goo.gl/maps/mpEqdhR5sdkJVSgbA'>📍Местоположение</a>
        ___________________
        Oстановка Президентская школа
        <a href='https://goo.gl/maps/b1BBmSXfzqCdAmuNA'>📍Местоположение</a>
        ___________________
        Юбилейная остановка
        <a href='https://goo.gl/maps/VXXQipsYtiGsfHR48'>📍Местоположение</a>
        ___________________
        Идеальная генерирующая остановка
        <a href='https://goo.gl/maps/SPNRdz1Z8g4AcbQ89'>📍Местоположение</a>
        ___________________
        Oстановка ТЕРДУ
        <a href='https://goo.gl/maps/eneVkAdyr3AvKGgJ9'>📍Местоположение</a>
        ___________________
        Oстановка Истикляль
        <a href='https://goo.gl/maps/jLgQPMZGkvo1tAnx7'>📍Местоположение</a>
        ___________________
        Стадион Сурхан остановка
        <a href='https://goo.gl/maps/J7DTDbmbtmbL1SnN9'>📍Местоположение</a>
        ___________________
        Oстановка колледжа олимпийского резерва
        <a href='https://goo.gl/maps/Gw7U6feQUQkmYSYn7'>📍Местоположение</a>
        ___________________
        Северный Автошохбекат (Зеленый мир)
        <a href='https://goo.gl/maps/c6rmMwhsSCVwCmqv9'>📍Местоположение</a>
        ___________________
        """
        bot.send_message(chat_id,text,parse_mode='HTML')
    db.save()


updater=Updater(token='')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,main))

updater.start_polling()
updater.idle()