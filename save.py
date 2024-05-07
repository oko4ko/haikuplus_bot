from enum import Enum
import json
class Message_type(Enum):
    haiku = 1
    ring = 2

def save(type:Message_type):
    file = __read__(type)


def __read__(type):
    if type == Message_type.haiku:
        with open('haiku.json', 'r') as f:
            return json.load(f)
    elif type == Message_type.ring:
        with open('ring.json', 'r') as f:
            return json.load(f)