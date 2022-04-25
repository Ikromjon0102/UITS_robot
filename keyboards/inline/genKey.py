from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.inline.yesno import answer_callback

genderKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text = "🧍‍♂️ Erkak", callback_data='male'),
        InlineKeyboardButton(text = "🧍‍♀️ Ayol", callback_data='female'),
    ]
]
)
ansdict = {
    "✔ ha":"yes",
    "❌ yo'q":"no"
}




answerKey = InlineKeyboardMarkup(row_width=2)
for key, value in ansdict.items():
    answerKey.insert(InlineKeyboardButton(text=key, callback_data=answer_callback.new(item_name=value)))

