from io import BytesIO

import aiohttp
from aiogram import types

from loader import bot


# download photo to telegraph and return link
async def get_link_photo(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file,
        )
        async with bot.session.post('https://telegra.ph/upload', data=form) as response:
            img_src = await response.json()
        link = 'https://telegra.ph' + img_src[0]['src']
        return link
