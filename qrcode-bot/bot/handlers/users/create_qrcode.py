from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from FSM.state import Form

from script.createqrcode import create

@dp.message_handler(commands=["create"], state='*')
async def command_addvk(message: Message, state: FSMContext):
    await message.answer('Напиши текст который будет в твоем Qr коде')
    await Form.Text.set()

@dp.message_handler(state=Form.Text)
async def answ(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    datanvalid = await state.get_data()
    data = datanvalid['text'] 

    id = message.from_user.id
    await state.finish()

    file = f"D:/qrcode-bot/create_qrcode/{id}.png"
    image = create(data, file)

    await message.answer(image)
    await bot.send_photo(id, types.InputFile(file))
    