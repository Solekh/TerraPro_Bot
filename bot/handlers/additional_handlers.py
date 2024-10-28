from datetime import datetime

from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __


from bot.buttons.reply import lang, registration_menu, cities, jins, main_menu
from bot.state import RegistrationStates
from db.models import User, LanguageEnum
from main import i18n

extra_router = Router()

@extra_router.message(F.text == "🛍 Заказать на сайте")
async def site_handler(message: Message):
    await message.answer("Для заказа, нажмите  (https://terrapro.uz/?utm_source=tgbot&utm_medium=knopka&utm_campaign=tgbot)")