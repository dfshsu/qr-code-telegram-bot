from aiogram.types import Message
from aiogram import types

from loader import dp

from script.getqrcode import main 

@dp.message_handler(commands=["upload"])
async def get_photo(message: types.Message):
    await message.answer('Отправь мне свой QR код')
    
@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    id = message.from_user.id

    file = f"D:/qrcode-bot/qr_code_photo/{id}.png"
    
    await message.photo[-1].download(file)
    text = main(file)
    await message.answer(text)
