from aiogram import types

from keyboards.default.start import contact
from loader import dp


@dp.message_handler(text='✍️ Ariza qoldirish')
@dp.message_handler(commands='contact')
async def send_contact(message: types.Message):
    await message.answer("Admin bilan bog'lanish uchun telefon raqamingizni qoldiring!",
                         reply_markup=contact)


@dp.message_handler(content_types='contact')
async def get_contact(message: types.Message):
    phone_number = message.contact.phone_number
    await message.reply(f"Sizning {phone_number} raqamingiz qabul qilindi!",
                         reply_markup=types.ReplyKeyboardRemove())
