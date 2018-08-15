import sys
import time
import logging
from pprint import pprint
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)

    if 'text' in msg:
        if msg['text']=='/remind':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text='吃藥', callback_data='吃藥'),
                    InlineKeyboardButton(text='運動', callback_data='運動'),
                    
                ],
                [
                    InlineKeyboardButton(text='睡覺', callback_data='睡覺'),
                    InlineKeyboardButton(text='其他', callback_data='其他'),
                ]
            ])
            bot.sendMessage(chat_id, '設定提醒', reply_markup=keyboard)

        
            
  

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    pprint(msg)

    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')
    


TOKEN ='666965847:AAHRWMV-Mb214AxImEIvU8uUs6w7eSaaIKc' 

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread(),
                 

print('Listening ...')
print('Listening ...')

while 1:
    time.sleep(10)