import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
import json
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="بدأ الفحص /START CHECK", callback_data="F1")
       
    M = types.InlineKeyboardButton('المطور', url='https://t.me/UT_UB')
    
    mas.add(A,M)
    
    bot.send_message(message.chat.id, f"CHECKER USERS INSTAGRAM BY AHMED️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="MohammedNajih":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="COINS INSTAUP|فحص نقاط انستا اب ", callback_data="F1")

		M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="-BOT CHECKER COINS INSTA APP \n -DEVLOPER MOHAMMED ALMUSWI \n -CHANEEL : @ONCLIK @ONCLCK \n -بوت فحص نقاط انستا اب \n -برمجه محمد الموسوي \n -اختر الطلب وسيتم الفحص حظا موفا ❤️",reply_markup=mas)

	elif call.data =="F1":
		while True:
			x1="".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
			x2="".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
			x3="".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
			x4="".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
			z1="".join(random.choice("1234567890")for i in range(1))
			z2="".join(random.choice("1234567890")for i in range(1))
			f1="".join(random.choice("_.")for i in range(1))
			f2="".join(random.choice("_.")for i in range(1))
			ok=0
			cp=0
			username=x1+x2+f1+z1+x4
			da = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7','content-length': '61','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/emailsignup/','sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(),'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M','x-instagram-ajax': '72bda6b1d047','x-requested-with': 'XMLHttpRequest'},data={'email' : '{username}@gmail.com','username': f'{username}','first_name': 'AA','opt_into_one_tap': 'false'}).text
			if (f'{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using {username}@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in  da:
				ok+=1
				bot.send_message(call.message.chat.id,f" ⌯ 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 ✅  \n︎ • ──────⚜────── • \n ⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 {username} \n • ──────⚜────── • \n ⌯ 𝙱𝚈 : @GDO_0 : @EP_EU ")
			else:
				cp+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
				mas.add(A,E,B,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="جاري الفحص النقاط ",reply_markup=mas)
					
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://checuesr.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
