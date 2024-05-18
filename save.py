from enum import Enum
import json


class MessageType(Enum):
    haiku = 1
    ring = 2


def save_art(message_type: MessageType, message, chat_id):
    data = __read__(message_type)
    chat_id = str(chat_id)
    if data.get(chat_id) is None:
        data[chat_id] = {"current_id": 1}
    data[chat_id][data[chat_id]["current_id"]] = message
    data[chat_id]["current_id"] += 1
    __write__(message_type, data)
    return data[chat_id]["current_id"] - 1


def get_art(message_type: MessageType, art_ids, chat_id, remove=False):
    chat_id = str(chat_id)
    if len(art_ids) == 0:
        if message_type == MessageType.haiku:
            return 'Ошибка: укажите ID хайку'
        else:
            return 'Ошибка: укажите ID обручального кольца'

    try:
        art_id = int(art_ids[0])
    except ValueError:
        return 'Ошибка: некорректный ID'

    if art_id <= 0:
        return 'Ошибка: некорректный ID'

    art_id = str(art_id)

    data = __read__(message_type)
    if data.get(chat_id) is None or data[chat_id].get(art_id) is None:
        return 'Ошибка: сообщения с указанным ID не существует, или оно было удалено'
    if remove:
        del data[chat_id][art_id]
        __write__(message_type, data)
        if message_type == MessageType.haiku:
            return 'Хайку удалено'
        else:
            return 'Кольцо удалено'
    else:
        return data[chat_id][art_id]


def get_art_id(message_type: MessageType, chat_id):
    data = __read__(message_type)
    if data.get(str(chat_id)) is None:
        return 1
    else:
        return int(data[str(chat_id)]["current_id"])


def __write__(message_type: MessageType, data):
    if message_type == MessageType.haiku:
        file_name = 'haiku.json'
    elif message_type == MessageType.ring:
        file_name = 'ring.json'
    else:
        raise ValueError('Invalid file type')
    with open(file_name, 'w') as f:
        json.dump(data, f)


def __read__(message_type):
    if message_type == MessageType.haiku:
        file_name = 'haiku.json'
    elif message_type == MessageType.ring:
        file_name = 'ring.json'
    else:
        raise ValueError('Invalid file type')
    with open(file_name, 'r') as f:
        return json.load(f)
