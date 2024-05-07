from enum import Enum
import json
class Message_type(Enum):
    haiku = 1
    ring = 2

def save(type:Message_type):
    file = __read__(type)


def __read__(type):
    if type == Message_type.haiku:
        file_name = 'haiku.json'
    elif type == Message_type.ring:
        file_name = 'ring.json'
    else:
        raise ValueError('Invalid file type')
    with open(file_name, 'r') as f:
        return json.load(f)