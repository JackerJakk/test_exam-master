from sqlite3 import adapt
from aiogram.fsm.state import StatesGroup

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from bot.states import BotState
from bot.utils_function import  check_user
from bot.buttons.reply import *

main_router = Router()

@main_router.message(BotState.language , F.text == __(main_panel_text) )
@main_router.message(BotState.language , F.text == __(main_panel_text) )
@main_router.message(CommandStart() )
async def command_start_handler(message: Message  , state : FSMContext) -> None:

    await check_user(message)
    await message.answer(_("Hello, {}".format(message.from_user.full_name)) , reply_markup=menu_buttons())
    # await state.clear()


@main_router.message(F.text == __(language_text))
async def command_start_handler(message: Message , state : FSMContext) -> None:
    await state.set_state(BotState.language)
    await message.answer(_("Choose language") , reply_markup=language_button())


@main_router.message(BotState.language , F.text.in_([uzb_text , en_text , ru_text]))
async def command_start_handler(message: Message, state: FSMContext , i18n) -> None:
    map_ = {uzb_text:"uz" , en_text:"en" , ru_text:"ru"}
    await state.set_data({"locale": map_.get(message.text)})
    i18n.current_locale = map_.get(message.text)
    await message.answer(_("Language was changed"), reply_markup=language_button())

@main_router.message(BotState.menu , F.text == __(menu_r) )
@main_router.message(BotState.menu , F.text == __(menu_r) )
@main_router.message(BotState.menu , F.text == __(menu_r) )
@main_router.message(BotState.menu , F.text == __(menu_r) )
@main_router.message(F.text == __(r_menu))
async def menu_handler(message: Message , state : FSMContext):
    await state.set_state(BotState.language)

    await message.answer(_('menu') , reply_markup=category_button())

@main_router.message(F.text == __(salad))
async def menu_handler(message: Message , state : FSMContext) :
    await state.set_state(BotState.menu)

    await message.answer(_('salads') , reply_markup=salad_button())


@main_router.message(F.text == __(f_food))
async def menu_handler(message: Message , state : FSMContext):
    await state.set_state(BotState.menu)

    await message.answer(_('fast foods') , reply_markup=fastf_button())



@main_router.message(F.text == __(h_food))
async def menu_handler(message: Message , state : FSMContext):
    await state.set_state(BotState.menu)

    await message.answer(_('hot meals') , reply_markup=hotf_button())























