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
        photo =  'AgACAgIAAxkBAAIBUmRV7djJlCczw1YgaBckR2Yh4U4rAALVyjEbAhyxSmnDOZss2faMAQADAgADcwADLwQ'
        bot.send_photo(chat_id,photo=photo,caption=text)
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
        Onkalogiya shifoxonasi bekati
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
        Olimpiada zaxiralar kolleji bekati
        <a href='https://goo.gl/maps/Gw7U6feQUQkmYSYn7'>📍Joylashuv</a>
        ___________________
        Shimoliy Avtoshoxbekati (Yashil Dunyo)
        <a href='https://goo.gl/maps/c6rmMwhsSCVwCmqv9'>📍Joylashuv</a>
        ___________________
        """
        bot.send_message(chat_id,text,parse_mode='HTML')
    elif data=='Об автобусном маршруте🗒':
        text = "Схема маршрута 15 автобусов (карта)"
        photo =  'AgACAgIAAxkBAAIBUmRV7djJlCczw1YgaBckR2Yh4U4rAALVyjEbAhyxSmnDOZss2faMAQADAgADcwADLwQ'
        bot.send_photo(chat_id,photo=photo,caption=text)
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
    elif data == "To'g'ri yo'nalish🚌":
        btn1=InlineKeyboardButton('Janubiy Avtoshoxbekat',callback_data='bek 1')
        btn2=InlineKeyboardButton('2-Akademik litsey bekati',callback_data='bek 2')
        btn3=InlineKeyboardButton('Hakim Termiziy masjidi bekati', callback_data='bek 3')
        btn4=InlineKeyboardButton('Mashhura klinikasi bekati',callback_data='bek 4')
        btn5=InlineKeyboardButton('Onkalogiya shifoxonasi bekati',callback_data='bek 5')
        btn6=InlineKeyboardButton('Temir yo\'l bekati',callback_data='bek 6')
        btn7=InlineKeyboardButton('Prezident maktabi bekati',callback_data='bek 7')
        nxt=InlineKeyboardButton('➡️',callback_data='next to')
        btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        bot.sendMessage(chat_id,text,reply_markup=btn)
    elif data == "Teskari yo'nalish🚌":
        btn1=InlineKeyboardButton("Shimoliy Avtoshoxbekati (Yashil Dunyo)",callback_data='bek 8')
        btn2=InlineKeyboardButton("Olimpiada zaxiralar kolleji bekati",callback_data='bek 9')
        btn3=InlineKeyboardButton("Surxon stadioni bekati",callback_data='bek 10')
        btn4=InlineKeyboardButton("Istiqlol bekati",callback_data='bek 11')
        btn5=InlineKeyboardButton("TERDU bekati",callback_data='bek 12')
        btn6=InlineKeyboardButton("Barkamol avlod bekati",callback_data='bek 13')
        btn7=InlineKeyboardButton("Yubleniy bekati",callback_data='bek 14')
        nxt=InlineKeyboardButton("➡️",callback_data='next tes')
        btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        bot.sendMessage(chat_id,text,reply_markup=btn)
    elif data == "Правильное направление🚌":
        btn1=InlineKeyboardButton('Термез Автошохбекат',callback_data='bek 1')
        btn2=InlineKeyboardButton('2-Академический лицей остановка',callback_data='bek 2')
        btn3=InlineKeyboardButton('Мечеть Хакима Термизи, остановка', callback_data='bek 3')
        btn4=InlineKeyboardButton('клиника Машхура',callback_data='bek 4')
        btn5=InlineKeyboardButton('Oнкологической больницы остановка',callback_data='bek 5')
        btn6=InlineKeyboardButton('Железнодорожная остановка',callback_data='bek 6')
        btn7=InlineKeyboardButton('Oстановка Президентская школа',callback_data='bek 7')
        nxt=InlineKeyboardButton('➡️',callback_data='next to')
        btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        bot.sendMessage(chat_id,text,reply_markup=btn)
    elif data == "Обратное направление🚌":
        btn1=InlineKeyboardButton('Северный Автошохбекат (Зеленый мир)',callback_data='bek 1')
        btn2=InlineKeyboardButton('Oстановка колледжа олимпийского резерва',callback_data='bek 2')
        btn3=InlineKeyboardButton('Стадион Сурхан остановка', callback_data='bek 3')
        btn4=InlineKeyboardButton('Oстановка Истикляль',callback_data='bek 4')
        btn5=InlineKeyboardButton('Oстановка ТЕРДУ',callback_data='bek 5')
        btn6=InlineKeyboardButton('Идеальная генерирующая остановка',callback_data='bek 6')
        btn7=InlineKeyboardButton('Юбилейная остановка',callback_data='bek 7')
        nxt=InlineKeyboardButton('➡️',callback_data='next tes')
        btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        bot.sendMessage(chat_id,text,reply_markup=btn)
    db.save()

def next(update:Update,context:CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    bot=context.bot
    _ , data = query.data
    db=DB('db.json')
    lang=db.get_lang(chat_id)
    if lang=="Uzbekcha🇺🇿":
        if data=='to':
            btn1=InlineKeyboardButton("Shimoliy Avtoshoxbekati (Yashil Dunyo)",callback_data='bek 8')
            btn2=InlineKeyboardButton("Olimpiada zaxiralar kolleji bekati",callback_data='bek 9')
            btn3=InlineKeyboardButton("Surxon stadioni bekati",callback_data='bek 10')
            btn4=InlineKeyboardButton("Istiqlol bekati",callback_data='bek 11')
            btn5=InlineKeyboardButton("TERDU bekati",callback_data='bek 12')
            btn6=InlineKeyboardButton("Barkamol avlod bekati",callback_data='bek 13')
            btn7=InlineKeyboardButton("Yubleniy bekati",callback_data='bek 14')
            back=InlineKeyboardButton("➡️",callback_data='back to')
            btn=InlineKeyboardMarkup([[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[btn1],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        else:
            btn1=InlineKeyboardButton('Janubiy Avtoshoxbekat',callback_data='bek 1')
            btn2=InlineKeyboardButton('2-Akademik litsey bekati',callback_data='bek 2')
            btn3=InlineKeyboardButton('Hakim Termiziy masjidi bekati', callback_data='bek 3')
            btn4=InlineKeyboardButton('Mashhura klinikasi bekati',callback_data='bek 4')
            btn5=InlineKeyboardButton('Onkalogiya shifoxonasi bekati',callback_data='bek 5')
            btn6=InlineKeyboardButton('Temir yo\'l bekati',callback_data='bek 6')
            btn7=InlineKeyboardButton('Prezident maktabi bekati',callback_data='bek 7')
            back=InlineKeyboardButton("➡️",callback_data='back tes')
            btn=InlineKeyboardMarkup([[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[btn1],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
    else:
        if data=='to':
            btn1=InlineKeyboardButton('Северный Автошохбекат (Зеленый мир)',callback_data='bek 1')
            btn2=InlineKeyboardButton('Oстановка колледжа олимпийского резерва',callback_data='bek 2')
            btn3=InlineKeyboardButton('Стадион Сурхан остановка', callback_data='bek 3')
            btn4=InlineKeyboardButton('Oстановка Истикляль',callback_data='bek 4')
            btn5=InlineKeyboardButton('Oстановка ТЕРДУ',callback_data='bek 5')
            btn6=InlineKeyboardButton('Идеальная генерирующая остановка',callback_data='bek 6')
            btn7=InlineKeyboardButton('Юбилейная остановка',callback_data='bek 7')
            back=InlineKeyboardButton("➡️",callback_data='back to')
            btn=InlineKeyboardMarkup([[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[btn1],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        else:
            btn1=InlineKeyboardButton('Термез Автошохбекат',callback_data='bek 1')
            btn2=InlineKeyboardButton('2-Академический лицей остановка',callback_data='bek 2')
            btn3=InlineKeyboardButton('Мечеть Хакима Термизи, остановка', callback_data='bek 3')
            btn4=InlineKeyboardButton('клиника Машхура',callback_data='bek 4')
            btn5=InlineKeyboardButton('Oнкологической больницы остановка',callback_data='bek 5')
            btn6=InlineKeyboardButton('Железнодорожная остановка',callback_data='bek 6')
            btn7=InlineKeyboardButton('Oстановка Президентская школа',callback_data='bek 7')
            back=InlineKeyboardButton("➡️",callback_data='back tes')
            btn=InlineKeyboardMarkup([[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[btn1],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)


updater=Updater(token='5796836647:AAF5s1LBPqGLElUUWNpAGWsIghr6_m4N0U8')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,main))

# updater.dispatcher.add_handler(MessageHandler(Filters.photo,img))

updater.start_polling()
updater.idle()