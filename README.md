A bot for detecting and haikus and wedding rings in Telegram messages.
A haiku is a message which can be divided into three lines with 5, 7 and 5 syllables respectfully
A ring is a message which is equirithmic to the line "обручальное кольцо"

Upon detecting a haiku or a ring, the bot replies to it and saves its text.
Previous haikus or rings may be requested by ID.
Adding rings manually is also supported.

Commands:
/info - Show info about the bot
/get_haiku - get haiku from its ID. (/get_haiku haiku_ID)
/get_ring - get ring from its ID. (/get_ring ring_ID)
/remove_haiku - get haiku from its ID. (/remove_haiku haiku_ID)
/remove_ring - get ring from its ID. (/remove_ring ring_ID)
/custom_ring - manually add a ring. This command must be a reply to a message.


Launch guide:
1. Create file config.py in root directory, put your Telegram API token there (token = "your_API_token")
2. Create files haiku.json and ring.json in root directory

Credits: Oleg Kochko

