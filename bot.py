import config
import telebot
import checks
from save import save_art, MessageType, get_art, get_art_id


def extract_arg(arg):
    return arg.split()[1:]


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message, 'Этот бот ищет случайные хайку и обручальные кольца в сообщениях.\n'
                          'Хайку - сообщение, которое можно разделить на 3 строчки по 5, 7 и 5 слогов\n'
                          'Кольцо - сообщение, эквиритмичное строчке \"Обручальное кольцо\"\n'
                          'Команды:\n'
                          '/info - показать информацию про бота\n'
                          '/get_haiku - получить хайку по ID. /get_haiku ID_хайку\n'
                          '/get_ring - получить кольцо по ID. /get_ring ID_кольца\n'
                          '/remove_haiku - удалить хайку по ID. /remove_haiku ID_хайку\n'
                          '/remove_ring - удалить кольцо по ID. /remove_ring ID_кольца\n'
                          '/custom_ring - добавление собственного кольца, не опознанного ботом')


@bot.message_handler(commands=["get_haiku"])
def get_haiku(message):
    art_ids = extract_arg(message.text)
    answer = get_art(MessageType.haiku, art_ids, message.chat.id)
    bot.reply_to(message, answer, parse_mode='Markdown')


@bot.message_handler(commands=["get_ring"])
def get_ring(message):
    art_ids = extract_arg(message.text)
    answer = get_art(MessageType.ring, art_ids, message.chat.id)
    bot.reply_to(message, answer, parse_mode='Markdown')


@bot.message_handler(commands=["remove_haiku"])
def get_haiku(message):
    art_ids = extract_arg(message.text)
    answer = get_art(MessageType.haiku, art_ids, message.chat.id, remove=True)
    bot.reply_to(message, answer, parse_mode='Markdown')


@bot.message_handler(commands=["remove_ring"])
def remove_ring(message):
    art_ids = extract_arg(message.text)
    answer = get_art(MessageType.ring, art_ids, message.chat.id, remove=True)
    bot.reply_to(message, answer, parse_mode='Markdown')


@bot.message_handler(commands=["custom_ring"])
def custom_ring(message):
    if message.reply_to_message:
        art_id = get_art_id(MessageType.ring, message.chat.id)
        ring_to_save = checks.add_info(
            telebot.formatting.mitalic(message.reply_to_message.text),
            message.from_user.username,
            art_id
        )
        save_art(MessageType.ring, ring_to_save, message.chat.id)
        bot.reply_to(message, f'Добавлено непростое украшенье #{art_id}', parse_mode='Markdown')
    else:
        bot.reply_to(message, "Команда должна быть ответом на сообщение", parse_mode='Markdown')


@bot.message_handler(content_types=["text"])
def message_answer(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'провода (извините)')
    haiku = checks.is_haiku(message.text)
    ring = checks.is_ring(message.text)
    if ring is not None:
        art_id = get_art_id(MessageType.ring, message.chat.id)
        answer = checks.add_info_unusual_decoration(telebot.formatting.mitalic('Непростое украшенье'),
                                                    message.from_user.username, art_id)
        ring_to_save = checks.add_info(telebot.formatting.mitalic(ring), message.from_user.username, art_id)
        save_art(MessageType.ring, ring_to_save, message.chat.id)
        bot.reply_to(message, answer, parse_mode='Markdown')
    if haiku is not None:
        art_id = get_art_id(MessageType.haiku, message.chat.id)
        answer = checks.add_info(telebot.formatting.mitalic(haiku), message.from_user.username, art_id)
        save_art(MessageType.haiku, answer, message.chat.id)
        print(answer)
        bot.reply_to(message, answer, parse_mode='Markdown')


if __name__ == '__main__':
    bot.infinity_polling()
