import telebot
from config import TOKEN, keys
from extensions import APIExcemption,Converter 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message): # блок ответа на команду
    bot.reply_to(message, f"Здравствуй, {message.from_user.first_name} {message.from_user.last_name}")
    text = 'Я рассчитываю и конвертирую разные валюты!\nЧто бы начать,введи запрос в следующем формате:\
\n<Название валюты,цену которой ты хочешь узнать>\
\n<Название валюты,относительно которой будем рассчитывать>\
\n<Количество переводимой валюты>\
\n Например: Рубль Доллар 1 \
\nЧто бы узнать список доступных команд введи: /help'
    bot.reply_to(message,text)

@bot.message_handler(commands=['help'])
def send_listCommands(message: telebot.types.Message):
    bot.reply_to(message, f"Вот список команд,с которыми я работаю:\n/start - перезапустить алгоритм и \
получить справку по функциям\n/values - список доступных для конвертации валют") 

@bot.message_handler(commands=['values'])
def send_listValues(message: telebot.types.Message):
    text = 'Пожалуйста,вводите каждую валюту с заглавной буквы и не добавляйте лишних символов.\nДоступные валюты:'
    for key in keys.keys():
        text ='\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text']) 
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIExcemption ('Количество параметров не соответствует формуле.\nДля обработки требуется 3 параметра')
        quote,base,amount = values
        convert_sum = Converter.get_price(quote,base,amount)
    except APIExcemption as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')
    except Exception:
        bot.reply_to(message,f'Не удалось обработать команду:\n{e}')
    else:
        indx_base = keys.get(base)
        text = f'Цена {amount} {quote} в {base} - {convert_sum} {indx_base}'
        bot.send_message(message.chat.id,text)






@bot.message_handler(content_types=['sticker','photo','emoji']) 
def send_unswer(message: telebot.types.Message): # блок ответа на контент
    bot.send_message(message.chat.id, 'Я пока не умею обрабатывать картинки :(')
@bot.message_handler(content_types=['voice']) 
def send_unswer(message: telebot.types.Message): # блок ответа на контент
    bot.send_message(message.chat.id, 'У тебя красивый голос!')

bot.polling(none_stop=True)