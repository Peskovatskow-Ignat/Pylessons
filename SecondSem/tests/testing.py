import telebot
import openai

bot = telebot.TeleBot("6122592866:AAF1vfrccpPgrM4DQBqXD6rx1IWtaLXS9qk")
openai.api_key = "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"

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

bot.polling()