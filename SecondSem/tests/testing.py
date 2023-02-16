import telegram
from telegram.ext import Updater, CommandHandler

# Функция-обработчик команды start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который может найти ID пользователя в Telegram. Просто отправь мне его имя пользователя.")

# Функция-обработчик команды find_id
def find_id(update, context):
    # Получаем имя пользователя из сообщения
    username = context.args[0]
    # Получаем информацию о пользователе
    user = context.bot.get_chat(username)
    # Отправляем ID пользователя
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"ID пользователя {username} - {user.id}")

# Токен бота
TOKEN = '6122592866:AAF1vfrccpPgrM4DQBqXD6rx1IWtaLXS9qk'

# Создаем объект updater
updater = Updater(TOKEN)

# Получаем объект диспетчера
dispatcher = updater.dispatcher

# Добавляем обработчик команды start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Добавляем обработчик команды find_id
find_id_handler = CommandHandler('find_id', find_id)
dispatcher.add_handler(find_id_handler)

# Запускаем бота
updater.start_polling()
