from telegram import Bot
import os
import requests

TOKEN = '5796836647:AAEF2c1SDvMn7QoeTa7-U-f3w08orRFMNvc'

bot = Bot('5796836647:AAEF2c1SDvMn7QoeTa7-U-f3w08orRFMNvc')

url = 'https://www.com'

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook", params={'url':url})
r = requests.get(f"https://api.telegram.org/bot{TOKEN}/GetWebhookInfo", params={'url':url})

print(r.json())