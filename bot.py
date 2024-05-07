import config
import telebot
import checks

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message, 'Этот бот ищет случайные хайку и обручальные кольца в сообщениях.')

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'провода (извините)')
    haiku = checks.is_haiku(message.text)
    ring = checks.is_ring(message.text)
    if ring is not None:
        bot.reply_to(message, checks.add_info(telebot.formatting.mitalic('Непростое украшенье'), message.from_user.username), parse_mode='Markdown')
    if haiku is not None:
        bot.reply_to(message, checks.add_info(telebot.formatting.mitalic(haiku), message.from_user.username), parse_mode='Markdown')

if __name__ == '__main__':
     bot.infinity_polling()