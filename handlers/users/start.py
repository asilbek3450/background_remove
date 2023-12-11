from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.start import start_keyboards
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Menyuni tanlang!", reply_markup=start_keyboards)


@dp.message_handler(text="📷 Remove BG")
async def bot_start(message: types.Message):
    await message.answer(f"Orqa fonini o'chirish uchun rasm yuboring!", reply_markup=types.ReplyKeyboardRemove())
