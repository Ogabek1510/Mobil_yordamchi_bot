from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🔵 Uzmobile'),
            KeyboardButton(text='🔴 Mobiuz')
        ],
        [
            KeyboardButton(text='🐝 Beeline'),
            KeyboardButton(text='🟣 Ucell')
        ],
    ],
    resize_keyboard=True
)