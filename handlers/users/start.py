from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKey import startKey
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, "
                         f" <a href='https://t.me/UIT_School'>Uchkurgan IT School</a>ning, "
                         f"rasmiy telegram botiga xush kelibsiz!\n"
                         f"ushbu bot orqali <b>IT Kurslar</b>ga ro'yxatdan o'tishingiz mumkin")
    await message.answer("Ro'yxatdan o'tish uchun <b>Contact</b>ingizni yuboring",
                         reply_markup=startKey)


@dp.message_handler(commands="html")
async def html(msg: types.Message):
    matn = "<b><i>Bu qalin matn</i></b>\n"
    matn += "<i>Bu qiyshiq matn</i>\n"
    matn += "<u>Bu tagiga chizilgan matn</u>\n"
    matn += "<s>Bu ustiga chizilgan matn</s>\n"
    matn += "<span class='tg-spoiler'>bu jibir jibir matn</span>\n"
    matn += "<a href='https://t.me/UIT_School'>UITSchool</a>\n"
    matn += "<code>print('Hello Python')</code>\n"
    await msg.answer(matn)

@dp.message_handler(commands="markdown")
async def html(msg: types.Message):
    matn = "*Bu qalin matn*\n"
    matn += "_Bu \#qiyshiq matn_\n"
    matn += "__Bu tagiga chizilgan matn__\n"
    matn += "~Bu ustiga chizilgan matn~\n"
    matn += "|| bu jibir jibir matn ||\n"
    matn += "[UITSchool](https://t.me/UIT_School)\n"
    matn += "`print('Hello Python')`\n"
    await msg.answer(matn,parse_mode="MarkdownV2")



