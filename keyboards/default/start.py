from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📷 Remove BG')],
    [KeyboardButton('✍️ Ariza qoldirish'), KeyboardButton('⚙️ Sozlamalar')]
])

contact = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📞 Telefon raqam yuborish', request_contact=True)]
])
