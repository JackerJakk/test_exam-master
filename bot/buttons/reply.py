from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _


language_text = "language"
uzb_text = "Uzbek"
en_text = "English"
ru_text = "Russian"
main_panel_text = "Main Panel"
r_menu = "menu of restaurant"
callus = "call us"
menu_r = "back to menu"
salad = 'Salads'
f_food = "Fast food"
h_food = 'hot dishes'
def make_reply(btns: list , size : list ,repeat=False):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*btns)
    if repeat:
        rkb.adjust(size[0] , repeat=True)
    else:
        rkb.adjust(size[0], repeat=True)
    return rkb.as_markup(resize_keyboard=True)


def menu_buttons():
    b1 = KeyboardButton(text=_("menu of restaurant")) # static
    b2 = KeyboardButton(text=_("call us"))
    b3 = KeyboardButton(text=_("language"))
    buttons = [b1 , b2 , b3]
    size = [2,1]
    return make_reply(buttons, size)


def language_button():
    btn1 = KeyboardButton(text="Uzbek")
    btn2 = KeyboardButton(text="English")
    btn3 = KeyboardButton(text="Russian")
    btn4 = KeyboardButton(text=_('Main Panel'))
    buttons = [btn1 , btn2 , btn3 , btn4]
    size = [3,1]
    return make_reply(buttons, size)

def category_button():
    btn1 = KeyboardButton(text=_("Salads"))
    btn2 = KeyboardButton(text=_("Fast food"))
    btn3 = KeyboardButton(text=_("hot dishes"))
    btn4 = KeyboardButton(text=_('Main Panel'))
    buttons = [btn1 , btn2 , btn3 , btn4]
    size = [3,1]
    return make_reply(buttons, size)


def salad_button():
    btn1 = KeyboardButton(text=_("Cezar"))
    btn2 = KeyboardButton(text=_("Olivye"))
    btn3 = KeyboardButton(text=_('back to menu'))
    buttons = [btn1 , btn2 , btn3 ]
    size = [2,1]
    return make_reply(buttons, size)


def fastf_button():
    btn1 = KeyboardButton(text=_("burger"))
    btn2 = KeyboardButton(text=_("hot dog"))
    btn3 = KeyboardButton(text=_('back to menu'))
    buttons = [btn1 , btn2 , btn3 ]
    size = [2,1]
    return make_reply(buttons, size)


def hotf_button():
    btn1 = KeyboardButton(text=_("palow"))
    btn2 = KeyboardButton(text=_("soup"))
    btn3 = KeyboardButton(text=_("back to menu"))
    buttons = [btn1 , btn2 , btn3 ]
    size = [2,1]
    return make_reply(buttons, size)

