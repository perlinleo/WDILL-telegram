import mylib as ml
import telebot
import os

from telebot import types
token = '415385336:AAG_0ZQJAF0DMMHyqMlZfBjvuJKfNKpLJ8k'
bot = telebot.TeleBot(token)
#path = '/root/env/megasuperfacedetectionbot/'
path = ""
admin_id = [296762765, 232673077]
@bot.message_handler(commands = ['start'])
def start(message):
        try:
                key = types.ReplyKeyboardMarkup(True, False)
                key.add(types.KeyboardButton('Привет, Бот!'))
                bot.send_message(message.chat.id, f"Привет, {message.json['from']['first_name']}!", reply_markup = key)
        except Exception as f:
                os.system(f"echo {f} >> logg.txt")

def feedback(message):
    bot.send_message(message.chat.id, "Спасибо за комментарий!")
    for x in admin_id:
        bot.send_message(x, message.text)
    text(message)
@bot.message_handler(content_types = ['text'])
def text(message):
        if message.text == 'Привет, Бот!':
            key = types.InlineKeyboardMarkup()
            key.add(types.InlineKeyboardButton("Отправить фото", callback_data='photofromuser'))
            key.add(types.InlineKeyboardButton("Feedback", callback_data='feedback'))
            key.add(types.InlineKeyboardButton("Донат", url='https://sobe.ru/na/dlya_fila'))
            bot.send_message(message.chat.id, "Я могу определить твою схожесть"
                                                  " с любым человеком!", reply_markup=key)

        else:
                pass

@bot.message_handler(content_types = ['photo'])
def send_photo(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_message(message.chat.id, "Отлично! Ваше фото на обработке!")
    with open("WDILL.jpg", 'wb') as file:
        try:
            file.write(downloaded_file)
            ml.splitIntoFaces.splitWDILL()
            ml.resize.resizeWDILL()
            #for i in checkGenerator.checkFace(getFinalFace=True,outputEveryLine=False):
                #print(i)
            for i in ml.checkGenerator.checkFace(getFinalFace=True,outputEveryLine=False):
                bot.send_message(message.chat.id, i)
                print(i)
            with open(f"{path}mostLikely.jpg","rb") as mostLikely:
                bot.send_photo(message.chat.id,mostLikely)
        except:
            bot.send_message(message.chat.id,"try another photo")

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton("Назад", callback_data='x'))
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception:
        pass
    if call.data == 'photofromuser':
        bot.send_message(call.message.chat.id, "Пришли фото!", reply_markup=key)
    elif call.data == 'x':
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
        text(call.message)
    elif call.data == 'feedback':
        bot.send_message(call.message.chat.id, "Напиши комментарий, который хочешь оставить:", reply_markup=key)
        bot.register_next_step_handler(call.message, feedback)
def polling():
        bot.polling()
if __name__ == '__main__':
        polling()

