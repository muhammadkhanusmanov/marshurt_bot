from telegram.ext import CommandHandler,MessageHandler,Filters,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
import os
from bott import start,main,admin,admin_command,bekat,next
from flask import Flask, request


Token=''


bot = Bot(Token)

app = Flask(__name__)


@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022'
    else:
        data = request.get_json(force = True)
        
        dispatcher: Dispatcher = Dispatcher(bot, update_queue=None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
                
        dispatcher.add_handler(CommandHandler('start',start))
        dispatcher.add_handler(MessageHandler(Filters.text('Admin paneli👤') | Filters.text('Панель администратора👤'),admin))
        dispatcher.add_handler(MessageHandler(Filters.text,main))
        dispatcher.add_handler(CallbackQueryHandler(next,pattern='next'))
        dispatcher.add_handler(CallbackQueryHandler(main,pattern='back'))
        dispatcher.add_handler(CallbackQueryHandler(bekat,pattern='bek'))
        dispatcher.add_handler(CallbackQueryHandler(admin_command,pattern='admin'))


        
        dispatcher.process_update(update)
        return 'ok'

if __name__=='__main__':
    app.run()