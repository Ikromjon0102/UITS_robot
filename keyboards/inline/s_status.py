from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

s_statusKey = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text = "Maktab o'quvchisi",
                             callback_data='school'),
    ],
    [
        InlineKeyboardButton(text = "Kollej/litsey",
                             callback_data='college'),
    ],
    [
        InlineKeyboardButton(text = "Talaba",
                             callback_data='student'),
    ],
    [
        InlineKeyboardButton(text = "Ishchi hodim",
                             callback_data='worker'),
    ],
    [
        InlineKeyboardButton(text = "Ishsiz fuqaro",
                             callback_data='eployer'),
    ],
    ]
)