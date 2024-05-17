from enum import Enum
import json
class Message_type(Enum):
    haiku = 1
    ring = 2

def save(type:Message_type, message):
    data = __read__(type)
    if data.get(message.chat.id) is None:
        data[message.chat.id] = {"current_id": 1}
    data[message.chat.id][data[message.chat.id]["current_id"]] = message.id
    data[message.chat.id]["current_id"] += 1
    __write__(type, data)

def __write__(type:Message_type, data):
    if type == Message_type.haiku:
        file_name = 'haiku.json'
    elif type == Message_type.ring:
        file_name = 'ring.json'
    else:
        raise ValueError('Invalid file type')
    with open(file_name, 'w') as f:
        json.dump(data, f)

def __read__(type):
    if type == Message_type.haiku:
        file_name = 'haiku.json'
    elif type == Message_type.ring:
        file_name = 'ring.json'
    else:
        raise ValueError('Invalid file type')
    with open(file_name, 'r') as f:
        return json.load(f)