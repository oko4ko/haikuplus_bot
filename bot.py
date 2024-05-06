import config
import telebot
import checks

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'провода (извините)')
    haiku = checks.is_haiku(message.text)
    if haiku is not None:
        bot.send_message(message.chat.id, checks.add_info(telebot.formatting.mitalic(haiku), message.from_user.username), parse_mode='Markdown')

if __name__ == '__main__':
     bot.infinity_polling()