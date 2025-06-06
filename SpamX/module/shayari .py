from SpamX import app
from pyrogram import filters
import random

SHAYARI_LIST = [
    "चलते-चलते यूँ ही किसी से मुलाकात हो जाए,\nजिंदगी से जिंदगी का सिलसिला चल निकले।",
    "दिल की बात होंठों पे लाना मुश्किल तो नहीं,\nबस थोड़ा सा हौसला चाहिए हंसने के लिए।",
    "ज़िंदगी में कुछ पाने के लिए कुछ खोना पड़ता है,\nपत्ते भी अगर हरा होना चाहते हैं,\nतो पुराने पत्तों को छोड़ना पड़ता है।"
]

@app.on_message(filters.command("shayari"))
async def shayari_command(client, message):
    random_shayari = random.choice(SHAYARI_LIST)
    await message.reply_text(random_shayari)
