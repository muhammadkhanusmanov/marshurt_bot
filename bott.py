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
    admins = db.get_admin()
    try:
        query = update.callback_query
        message_id = query.message.message_id
        chat_id = query.message.chat_id
        bot=context.bot
        _ , data = query.data.split()
    except:
        bot=context.bot
        message_id=update.message.message_id
        chat_id=update.message.chat_id
        data=update.message.text
    lang=db.get_lang(chat_id)
    if str(chat_id) in admins:
        try:
            a,b=data.split('=')
            if lang=='Uzbekcha🇺🇿':
                if a=='Interval':
                    db.upd(inter=b)
                    bot.send_message(chat_id,f'Interval vaqt yangilandi✅\nYangilanggan vaqt: {b}')
                elif a=='start':
                    db.upd(start=b)
                    bot.send_message(chat_id,f'Xarakat boshlanish vaqti yangilandi✅\nYangilanggan vaqt: {b}')
                elif a=='end':
                    db.upd(end=b)
                    bot.send_message(chat_id,f'Xarakat tugash vaqti yangilandi✅\nYangilanggan vaqt: {b}')
                elif a=='add':
                    val=db.add_admin(b)
                    if not val:
                        bot.send_message(chat_id,f'Bu foydalanuvchi allaqachon admin')
                    else:
                        bot.send_message(chat_id,f'Admin qo\'shildi✅\nuser_id: {b}')
                elif a=='del':
                    val=db.del_admin(b)
                    if not val:
                        bot.send_message(chat_id,f'Bu foydalanuvchi topilmadi')
                    else:
                        bot.send_message(chat_id,f'Admin o\'chirildi✅\nuser_id: {b}')
            else:

                if a=='Interval':
                    db.upd(inter=b)
                    bot.send_message(chat_id,f'Время интервала обновлено ✅\nОбновлено время: {b}')
                elif a=='start':
                    db.upd(start=b)
                    bot.send_message(chat_id,f'Обновлено время начала действия ✅\nОбновлено время: {b}')
                elif a=='end':
                    db.upd(end=b)
                    bot.send_message(chat_id,f'Время окончания действия обновлено ✅\nОбновлено время: {b}')
                elif a=='add':
                    val=db.add_admin(b)
                    if not val:
                        bot.send_message(chat_id,f'Этот пользователь уже является администратором')
                    else:
                        bot.send_message(chat_id,f'Администратор добавил ✅\nuser_id: {b}')
                elif a=='del':
                    val=db.del_admin(b)
                    if not val:
                        bot.send_message(chat_id,f'Этот пользователь не найден')
                    else:
                        bot.send_message(chat_id,f'Администратор удалил ✅\nuser_id: {b}')
        except:
            pass



    if data=='Uzbekcha🇺🇿':
        db.add_lang('Uzbekcha🇺🇿',chat_id)
        bot.send_message(chat_id,'Asosiy menu')
        text="15-avftobusning siz uchun kerakli yo'nalishini tanlif lang\n\n*To'g'ri yo'nalish yo'nalish:\n📍Termiz Avtoshoxbekat ➡️ 📍Shimoliy Avtoshoxbekat (Yashil Dunyo)\n\n*Teskari yo'nalish: 📍Shimoliy Avtoshoxbekat (Yashil Dunyo) ➡️ 📍Termiz Avtoshoxbekat"
        if str(chat_id) in admins:
            btn=ReplyKeyboardMarkup([["To'g'ri yo'nalish🚌", "Teskari yo'nalish🚌"],['Avftobus yo\'nalishi haqida🗒'],['Admin paneli👤']],resize_keyboard=True)
        else:
            btn=ReplyKeyboardMarkup([["To'g'ri yo'nalish🚌", "Teskari yo'nalish🚌"],['Avftobus yo\'nalishi haqida🗒']],resize_keyboard=True)
        bot.send_message(chat_id,text=text,reply_markup=btn)
    elif data == 'Русский🇷🇺':
        db.add_lang('Русский🇷🇺',chat_id)
        bot.send_message(chat_id,'Главное меню')
        text="Выберите нужное Вам направление 15-авфтобуса\n\n*Правильное направление:\n📍Термиз Автошохбекат ➡️ 📍Северный Автошохбекат (Яшил Дуне)\n\n*Обратное направление: 📍Северный Автошохбекат (Яшил Дуне) ➡️ 📍 Термез Автошохбекат"
        if str(chat_id) in admins:
            btn=ReplyKeyboardMarkup([["Правильное направление🚌", "Обратное направление🚌"],['Об автобусном маршруте🗒'],['Панель администратора👤']],resize_keyboard=True)
        else:
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
    if data == "To'g'ri yo'nalish🚌" or data == "to":
        btn2=InlineKeyboardButton('2-Akademik litsey bekati',callback_data='bek t,1')
        btn3=InlineKeyboardButton('Hakim Termiziy masjidi bekati', callback_data='bek t,2')
        btn4=InlineKeyboardButton('Mashhura klinikasi bekati',callback_data='bek t,3')
        btn5=InlineKeyboardButton('Spit despanseri bekati',callback_data='bek t,4')
        btn6=InlineKeyboardButton('Onkalogiya shifoxonasi bekati',callback_data='bek t,5')
        btn7=InlineKeyboardButton('Temir yo\'l bekati',callback_data='bek t,6')
        btn8=InlineKeyboardButton('Prezident maktabi bekati',callback_data='bek t,7')
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        if data=='to' and lang=="Uzbekcha🇺🇿":
            nxt=InlineKeyboardButton('➡️',callback_data='next to')
            btn=InlineKeyboardMarkup([[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[btn8],[nxt]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        elif data!='to':
            nxt=InlineKeyboardButton('➡️',callback_data='next to')
            btn=InlineKeyboardMarkup([[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[btn8],[nxt]])
            bot.sendMessage(chat_id,text,reply_markup=btn)
    if data == "Teskari yo'nalish🚌" or data == "tes":
        btn1=InlineKeyboardButton("Yashil Dunyo bekati",callback_data='bek s,1')
        btn2=InlineKeyboardButton("Olimpiada zaxiralar kolleji bekati",callback_data='bek s,2')
        btn3=InlineKeyboardButton("Surxon stadioni bekati",callback_data='bek s,3')
        btn4=InlineKeyboardButton("Istiqlol bekati",callback_data='bek s,4')
        btn5=InlineKeyboardButton("TERDU bekati",callback_data='bek s,5')
        btn6=InlineKeyboardButton("Barkamol avlod bekati",callback_data='bek s,6')
        btn7=InlineKeyboardButton("Yubleniy bekati",callback_data='bek s,7')
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        if data=='tes'and lang=='Uzbekcha🇺🇿':
            nxt=InlineKeyboardButton("➡️",callback_data='next tes')
            btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        elif data!='tes':
            nxt=InlineKeyboardButton("➡️",callback_data='next tes')
            btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
            bot.sendMessage(chat_id,text,reply_markup=btn)
    if data == "Правильное направление🚌" or data == "to":
        btn2=InlineKeyboardButton('2-Академический лицей остановка',callback_data='bek t,1')
        btn3=InlineKeyboardButton('Мечеть Хакима Термизи, остановка', callback_data='bek t,2')
        btn4=InlineKeyboardButton('клиника Машхура',callback_data='bek t,3')
        btn5=InlineKeyboardButton('Коса Диспансерная Станция остановка',callback_data='bek t,4')
        btn6=InlineKeyboardButton('Oнкологической больницы остановка',callback_data='bek t,5')
        btn7=InlineKeyboardButton('Железнодорожная остановка',callback_data='bek t,6')
        btn8=InlineKeyboardButton('Oстановка Президентская школа',callback_data='bek t,7')
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        if data=='to' and lang=='Русский🇷🇺':
            nxt=InlineKeyboardButton("➡️",callback_data='next to')
            btn=InlineKeyboardMarkup([[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[btn8],[nxt]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        elif data!='to':
            nxt=InlineKeyboardButton("➡️",callback_data='next to')
            btn=InlineKeyboardMarkup([[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[btn8],[nxt]])
            bot.sendMessage(chat_id,text,reply_markup=btn)
    if data == "Обратное направление🚌" or data == "tes":
        btn1=InlineKeyboardButton('Зеленый мир остановка',callback_data='bek s,1')
        btn2=InlineKeyboardButton('Oстановка колледжа олимпийского резерва',callback_data='bek s,2')
        btn3=InlineKeyboardButton('Стадион Сурхан остановка', callback_data='bek s,3')
        btn4=InlineKeyboardButton('Oстановка Истикляль',callback_data='bek s,4')
        btn5=InlineKeyboardButton('Oстановка ТЕРДУ',callback_data='bek 5')
        btn6=InlineKeyboardButton('Идеальная генерирующая остановка',callback_data='bek s,6')
        btn7=InlineKeyboardButton('Юбилейная остановка',callback_data='bek s,7')
        text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
        if data=='tes' and lang=='Русский🇷🇺':
            nxt=InlineKeyboardButton("➡️",callback_data='next tes')
            btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        elif data!='tes':
            nxt=InlineKeyboardButton("➡️",callback_data='next tes')
            btn=InlineKeyboardMarkup([[btn1],[btn2],[btn3],[btn4],[btn5],[btn6],[btn7],[nxt]])
            bot.sendMessage(chat_id,text,reply_markup=btn)
    db.save()

def next(update:Update,context:CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    bot=context.bot
    _ , data = query.data.split()
    db=DB('db.json')
    lang=db.get_lang(chat_id)
    if lang=="Uzbekcha🇺🇿":
        if data=='to':
            btn1=InlineKeyboardButton("Yashil Dunyo bekati",callback_data='bek t,14')
            btn2=InlineKeyboardButton("Olimpiada zaxiralar kolleji bekati",callback_data='bek t,13')
            btn3=InlineKeyboardButton("Surxon stadioni bekati",callback_data='bek t,12')
            btn4=InlineKeyboardButton("Istiqlol bekati",callback_data='bek t,11')
            btn5=InlineKeyboardButton("TERDU bekati",callback_data='bek t,10')
            btn6=InlineKeyboardButton("Barkamol avlod bekati",callback_data='bek t,9')
            btn7=InlineKeyboardButton("Yubleniy bekati",callback_data='bek t,8')
            back=InlineKeyboardButton("⬅️",callback_data='back to')
            btn=InlineKeyboardMarkup([[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[btn1],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        else:
            btn2=InlineKeyboardButton('2-Akademik litsey bekati',callback_data='bek s,14')
            btn3=InlineKeyboardButton('Hakim Termiziy masjidi bekati', callback_data='bek s,13')
            btn4=InlineKeyboardButton('Mashhura klinikasi bekati',callback_data='bek s,12')
            btn5=InlineKeyboardButton('Spit despanseri bekati',callback_data='bek s,11')
            btn6=InlineKeyboardButton('Onkalogiya shifoxonasi bekati',callback_data='bek s,10')
            btn7=InlineKeyboardButton('Temir yo\'l bekati',callback_data='bek s,9')
            btn8=InlineKeyboardButton('Prezident maktabi bekati',callback_data='bek s,8')
            back=InlineKeyboardButton("⬅️",callback_data='back tes')
            btn=InlineKeyboardMarkup([[btn8],[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
    else:
        if data=='to':
            btn1=InlineKeyboardButton('Зеленый мир остановка',callback_data='bek t,14')
            btn2=InlineKeyboardButton('Oстановка колледжа олимпийского резерва',callback_data='bek t,13')
            btn3=InlineKeyboardButton('Стадион Сурхан остановка', callback_data='bek t,12')
            btn4=InlineKeyboardButton('Oстановка Истикляль',callback_data='bek t,11')
            btn5=InlineKeyboardButton('Oстановка ТЕРДУ',callback_data='bek t,10')
            btn6=InlineKeyboardButton('Идеальная генерирующая остановка',callback_data='bek t,9')
            btn7=InlineKeyboardButton('Юбилейная остановка',callback_data='bek t,8')
            back=InlineKeyboardButton("⬅️",callback_data='back to')
            btn=InlineKeyboardMarkup([[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[btn1],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
        else:
            btn2=InlineKeyboardButton('2-Академический лицей остановка',callback_data='bek s,14')
            btn3=InlineKeyboardButton('Мечеть Хакима Термизи, остановка', callback_data='bek s,13')
            btn4=InlineKeyboardButton('клиника Машхура',callback_data='bek t,12')
            btn5=InlineKeyboardButton('Коса Диспансерная Станция остановка',callback_data='bek t,11')
            btn6=InlineKeyboardButton('Oнкологической больницы остановка',callback_data='bek t,10')
            btn7=InlineKeyboardButton('Железнодорожная остановка',callback_data='bek t,9')
            btn8=InlineKeyboardButton('Oстановка Президентская школа',callback_data='bek t,8')
            text="Kerakli bekatni kiriting va avftobusning taxminiy kelish vaqtini oling"
            back=InlineKeyboardButton("⬅️",callback_data='back tes')
            btn=InlineKeyboardMarkup([[btn8],[btn7],[btn6],[btn5],[btn4],[btn3],[btn2],[back]])
            bot.edit_message_reply_markup(chat_id,message_id,reply_markup=btn)
    db.save()
 
def bekat(update:Update,context:CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    bot=context.bot
    _ , data = query.data.split()
    db=DB('db.json')
    lang=db.get_lang(chat_id)
    togri=db.get_loc('to')
    teskari=db.get_loc('tes')
    yu,bek=data.split(',')
    date=query.message.date
    print(date)
    # text='Adminni o\'chirish uchun quyidagicha yuboring del=user_id'
    bot.delete_message(chat_id=chat_id,message_id=message_id)
    if lang == 'Uzbekcha🇺🇿':
        if yu == 't':
            t=db.main(date,bek,'to\'g\'ri')
            lat,lang=togri[int(bek)-1].split(',')
            bot.send_location(chat_id,lat,lang)
            text=f'🚌Avftobusning taxminiy kelish vaqti:\n_________\n⏰ {t} (±1 daqiqa)'
            bot.send_message(chat_id=chat_id,text=text)
        else:
            t=db.main(date,bek,'teskari')
            lat,lang=teskari[int(bek)-1].split(',')
            bot.send_location(chat_id,lat,lang)
            text=f'🚌Avftobusning taxminiy kelish vaqti:\n_________\n⏰ {t} (±1 daqiqa)'
            bot.send_message(chat_id=chat_id,text=text)
    else:
        if yu == 't':
            t=db.main(date,bek,'to\'g\'ri')
            lat,lang=togri[int(bek)-1].split(',')
            bot.send_location(chat_id,lat,lang)
            text=f'🚌 Расчетное время прибытия автобуса:\n_________\n⏰ {t} (±1 минута)'
            bot.send_message(chat_id=chat_id,text=text)
        else:
            t=db.main(date,bek,'teskari')
            lat,lang=teskari[int(bek)-1].split(',')
            bot.send_location(chat_id,lat,lang)
            text=f'🚌 Расчетное время прибытия автобуса:\n_________\n⏰ {t} (±1 минута)'
            bot.send_message(chat_id=chat_id,text=text)
    db.save()

def admin(update:Update,context:CallbackContext):
    bot=context.bot
    message_id=update.message.message_id
    chat_id=update.message.chat_id
    db=DB('db.json')
    lang=db.get_lang(chat_id)
    admins=db.get_admin()
    if str(chat_id) in admins:
        if lang=='Uzbekcha🇺🇿':
            btn1=InlineKeyboardButton('Oraliq vaqtni o\'zgartirish', callback_data='admin intertval')
            btn2=InlineKeyboardButton('To\'xtash vaqtini o\'zgartirish', callback_data='admin end')
            btn3=InlineKeyboardButton('Boshlash vaqtini o\'zgartirish', callback_data='admin start')
            btn4=InlineKeyboardButton('Admin qo\'shish', callback_data='admin add')
            btn5=InlineKeyboardButton('Admin o\'chirish', callback_data='admin del')
            btn6=InlineKeyboardButton('Malumot', callback_data='admin about')
            btn=InlineKeyboardMarkup([[btn2,btn3],[btn1,btn4],[btn5,btn6]])
            text="Admin sozlamalari⚙️"
            bot.sendMessage(chat_id, text,reply_markup=btn)    
        else:
            btn1=InlineKeyboardButton('Изменить время интервала', callback_data='admin intertval')
            btn2=InlineKeyboardButton('Изменить время остановки', callback_data='admin end')
            btn3=InlineKeyboardButton('Изменить время начала', callback_data='admin start')
            btn4=InlineKeyboardButton('Добавить администратора', callback_data='admin add')
            btn5=InlineKeyboardButton('Удалить администратора', callback_data='admin del')
            btn6=InlineKeyboardButton('Информация', callback_data='admin about')
            btn=InlineKeyboardMarkup([[btn2,btn3],[btn1,btn4],[btn5,btn6]])
            text="Настройки администратора⚙️"
            bot.sendMessage(chat_id, text,reply_markup=btn)

def admin_command(update:Update,context:CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    bot=context.bot
    _ , data = query.data.split()
    db=DB('db.json')
    lang=db.get_lang(chat_id)
    if lang=='Uzbekcha🇺🇿':
        if data=='interval':
            text="Avftobuslar orasidagi vaqt intaervalini o'zgartirish uchun quyidagicha yuboring Interval=vaqt (minutda)"
        elif data=='start':
            text = 'Avftobuslar xarakatining boshlanish vaqtini o\'zgartirish uchun quyidagicha yuboring start=vaqt (hh:mm)'
        elif data=='end':
            text = 'Avftobuslar xarakatining to\'xtash vaqtini o\'zgartirish uchun quyidagicha yuboring end=vaqt (hh:mm)'
        elif data=='add':
            text='Admin qo\'shish uchun quyidagicha yuboring add=user_id'
        elif data=='about':
            q,w,e,r=db.get_about()
            text = f"Admins: {r}\n\nInterval time: {q}\n\nStart time: {w}\n\nEnd time: {e}"
        else:
            text='Adminni o\'chirish uchun quyidagicha yuboring del=user_id'
        bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=text)
    else:
        if data=='interval':
            text="Чтобы изменить временной интервал между автобусами, отправьте Interval=время (в минутах)"
        elif data=='start':
            text = 'Чтобы изменить время начала автобусного сообщения, отправьте start=время (hh:mm)'
        elif data=='end':
            text = 'Чтобы изменить время автобусной остановки, отправьте end=время (hh:mm)'
        elif data=='add':
            text='Чтобы добавить администратора, отправьте add=user_id'
        elif data=='about':
            q,w,e,r=db.get_about()
            text = f"Admins: {r}\n\nInterval time: {q}\n\nStart time: {w}\n\nEnd time: {e}"
        else:
            text='Чтобы удалить администратора, отправьте del=user_id'
        bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=text)




# updater=Updater(token=Token)
# updater.dispatcher.add_handler(CommandHandler('start',start))
# updater.dispatcher.add_handler(MessageHandler(Filters.text('Admin paneli👤') | Filters.text('Панель администратора👤'),admin))
# updater.dispatcher.add_handler(MessageHandler(Filters.text,main))
# updater.dispatcher.add_handler(CallbackQueryHandler(next,pattern='next'))
# updater.dispatcher.add_handler(CallbackQueryHandler(main,pattern='back'))
# updater.dispatcher.add_handler(CallbackQueryHandler(bekat,pattern='bek'))
# updater.dispatcher.add_handler(CallbackQueryHandler(admin_command,pattern='admin'))

# # updater.dispatcher.add_handler(MessageHandler(Filters.photo,img))

# updater.start_polling()
# updater.idle()