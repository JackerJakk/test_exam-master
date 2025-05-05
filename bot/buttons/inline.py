from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def help_buttons():
    ikb = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text='Contact us ', url='https://t.me/JackerJakk')
    )


