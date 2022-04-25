from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

proKey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🐍 Python',callback_data="py"),
        ],
        [
            InlineKeyboardButton(text='🕸 WEB',callback_data="web")
        ],
        [
            InlineKeyboardButton(text="🎨 Photoshop",
                                 callback_data="pshop")
        ],
        [
            InlineKeyboardButton(text="✒ 3dsMAX",
                                 callback_data="3ds")
        ],
        [
            InlineKeyboardButton(text="💻 Savodxonlik",
                                 callback_data="cs")
        ],
        [
            InlineKeyboardButton(text="✈ IT English",
                                 callback_data="eng"),
        ],
        [
            InlineKeyboardButton(text="📐 IT Matem",
                                 callback_data="math")
        ],
        # [
        #     InlineKeyboardButton(text=" Chanel",
        #                          url="https://t.me/UIT_School"),
        #     InlineKeyboardButton(text="Group",
        #                          url="https://t.me/UITS_live_chat")
        # ],
        # [
        #     InlineKeyboardButton(text=" Share",
        #         switch_inline_query="Zo'r bot ekan"),
        # ],
    ]
)




