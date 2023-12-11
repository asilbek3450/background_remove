from aiogram import types

from loader import dp
from utils.remove_back import background_remove
from utils.link_photo import get_link_photo


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video_handler(message: types.Message):
    # await message.video.download()
    await message.answer("Video qabul qilindi")


# @dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(message: types.Message):
    photo = message.photo[-1]
    link = await get_link_photo(photo)
    await message.answer(link)
    # await message.answer_photo(link)
    r_photo = await background_remove(link)
    await message.reply_document(r_photo, caption='Fon olib tashlandi')
