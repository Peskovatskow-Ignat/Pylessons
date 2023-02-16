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
users = [763008655, 809296638, 908009390, 1755846502]


async def send_messages():
    # отправляем сообщение каждому пользователю
    for user in users:
        # генерируем случайное слово из списка
        words = ['прекрасного', 'восхитительного', 'чудесного']
        word = random.choice(words)
        complements = ["Любимая", "Солнышко", "Зайчик", "Медвежонок"]
        complement = random.choice(complements)

        # отправляем сообщение
        message = f'Доброе уторо, {complement}♥! Желаю тебе {word} дня!'
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


bot.polling(none_stop=True, interval=0)