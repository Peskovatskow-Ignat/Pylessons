import telegram
import random
import asyncio
import telebot
from telegram.ext import Updater, MessageHandler, filters
import os
from fuzzywuzzy import fuzz

# замените 'TOKEN' на токен своего бота
bot = telegram.Bot(token='6122592866:AAF1vfrccpPgrM4DQBqXD6rx1IWtaLXS9qk')

# список пользователей, которым нужно отправить сообщение
users = [763008655, 812819649, 809296638, 908009390, 1755846502, 1474001277]


async def send_messages():
    # отправляем сообщение каждому пользователю
    for user in users:
        # генерируем случайное слово из списка
        words = ['прекрасного', 'восхитительного', 'чудесного']
        word = random.choice(words)
        complements = ["Арестанты", "Кентики", "Бродяги", "Фартовые"]
        complement = random.choice(complements)

        # отправляем сообщение
        message = f'Утро Бодрое {complement}! Давай напиши мне что-то или зубы в клочья полетят!'
        await bot.send_message(chat_id=user, text=message)

async def send_messages_2():
    # отправляем сообщение каждому пользователю
    for user in users:
        # генерируем случайное слово из списка
        words = ['бродяги', 'кентики', 'братва']
        word = random.choice(words)
        complements = ["Счастья здоровья", "Удачи", "Деняг"]
        complement = random.choice(complements)

        # отправляем сообщение
        message = f'Короче ,{word}, я погнал ежже. {complement} вам'
        await bot.send_message(chat_id=user, text=message)


# запускаем асинхронную функцию с помощью asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(send_messages())

# Создаем экземпляр бота
bot = telebot.TeleBot('6122592866:AAF1vfrccpPgrM4DQBqXD6rx1IWtaLXS9qk')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Браток я тут, что тебе понадобилось')

@bot.message_handler(commands=["menu"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Короче без обид, но я пока что глупенький')


mas=[]
if os.path.exists(r'D:\pythonProject\python\SecondSem\tests\boltun.txt') == True:
    print(True)
    f=open(r'D:\pythonProject\python\SecondSem\tests\boltun.txt', 'r+', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()
else:
    print("Я не вижу")

# С помощью fuzzywuzzy определяем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка

def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists(r'D:\pythonProject\python\SecondSem\tests\boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # Изучаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Не смог'
    except:
        return 'Ошибка'
    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Запись ответа
    s = answer(message.text)
    # Отправка ответа
    bot.send_message(message.chat.id, s)

# Запускаем бота
bot.polling(none_stop=True, interval=0)

loop_2 = asyncio.get_event_loop()
loop.run_until_complete(send_messages_2())
