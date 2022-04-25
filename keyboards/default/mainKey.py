from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact",request_contact=True),
            # KeyboardButton(text="location",request_location=True),
        ]
    ], resize_keyboard=True
)
mainKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Qo'llanma"),
        ]
    ], resize_keyboard=True
)