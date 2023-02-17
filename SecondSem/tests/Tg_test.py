import telegram
import random
import asyncio
import telebot
import openai
from telebot import types

# замените 'TOKEN' на токен своего бота
bot = telegram.Bot(token='6122592866:AAF1vfrccpPgrM4DQBqXD6rx1IWtaLXS9qk')
openai.api_key = "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"

# список пользователей, которым нужно отправить сообщение
users = [763008655]


async def send_messages():
    # отправляем сообщение каждому пользователю
    for user in users:
        # генерируем случайное слово из списка
        words = ['прекрасного', 'восхитительного', 'чудесного']
        word = random.choice(words)
        complements = ["Арестанты", "Кентики", "Бродяги", "Фартовые"]
        complement = random.choice(complements)

        # отправляем сообщение
        message = f'Утро Бодрое {complement}! Давай напиши мне что-то, я стал умнее'
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

@bot.message_handler(commands=['meny'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton('/school')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(commands = ["school"])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Получай бро: ', url='https://class.sirius.ru/journal-schedule-action/u.1693')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на Cириус журнал", reply_markup = markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = f"{message.text}",
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

# Запускаем бота
bot.polling()
