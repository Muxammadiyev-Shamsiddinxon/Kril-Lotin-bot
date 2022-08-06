
from loader import dp

from aiogram import Bot, Dispatcher, executor, types

# kril lotin kutubxonalari
from handlers.transliterate import to_cyrillic,to_latin




@dp.message_handler()
async def imlo_bot(message: types.Message):
    xabar = message.text
    if xabar.isascii():
        javob = f"<code>{to_cyrillic(xabar)}</code>"

    else:
        javob = f"<code>{to_latin(xabar)}</code>"

    await message.reply(javob)


