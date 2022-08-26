from aiogram.types import Message
from aiogram import types

from loader import dp

@dp.message_handler(commands=["start"])
async def get_photo(message: types.Message):
    await message.answer('Напиши /upload или просто отправь мне Qr код!')