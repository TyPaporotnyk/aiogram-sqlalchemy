from aiogram import types


def get_start_keyboard():
    buttons = [
        [types.KeyboardButton(text="Автори")],
        [types.KeyboardButton(text="Статус")],
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons)
    return keyboard
