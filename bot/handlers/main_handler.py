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

main_router = Router()

text1 = """ 🙋‍♂️🙋‍♀️, Мы рады видеть вас в числе наших покупателей. С помощью этого бота вы можете:

- Пользоваться накопительной картой, проверить баланс и историю карты, использовать ее при   следующей покупки, показав штрих-код кассиру. 💳🛍️
- Оставлять отзыв или обратную связь 💬
- Заказать доставку одежды не выходя из телеграма 🚚👕
- Быть в курсе новых поступлений и эксклюзивных акций. 🛒💰
- Узнать адреса и контакты наших магазинов. 📍📞
- Получить информацию по актуальным вакансиям в нашей компании. 💼👔"""

text2 = """
Здравствуйте! 🌟 Давайте для начала выберем язык обслуживания! 🌐

Assalomu aleykum! 🌟 Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik. 🌐

Choose a language, please
"""

text3 = """
Для авторизации в нашей программе лояльности, пожалуйста, введите номер телефона 📱.
Это позволит вам накапливать баллы в размере до 7% от суммы каждой покупки 🎁🛒.
"""


@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    user = await User().get(id_=message.from_user.id)
    if user:
        await message.answer(f"{user.name} {text1}", reply_markup=main_menu())
    else:
        await message.answer(text2, reply_markup=lang())
        await state.set_state(RegistrationStates.lang)

@main_router.message(F.text.in_({"Русский 🇷🇺", "O'zbek 🇺🇿"}), RegistrationStates.lang)
async def lang_handler(message: Message, state: FSMContext) -> None:
    lang = LanguageEnum(message.text).name
    i18n.current_locale = lang
    await state.update_data({"locale": lang})
    await state.set_state(RegistrationStates.phone)
    await message.answer(text3, reply_markup=registration_menu())

@main_router.message(RegistrationStates.phone)
async def phone_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(RegistrationStates.city)
    await message.answer("Выберите город", reply_markup=cities())

@main_router.message(RegistrationStates.city)
async def city_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(city=message.text)
    await state.set_state(RegistrationStates.jins)
    await message.answer("Укажите свой пол: ", reply_markup=jins())

@main_router.message(RegistrationStates.jins)
async def jins_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(jins=message.text)
    await state.set_state(RegistrationStates.name)
    await message.answer("Напишите Ваше имя: ✍️: ")

@main_router.message(RegistrationStates.name)
async def name_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer("Введите дату рождения (пример 1993.01.31):")
    await state.set_state(RegistrationStates.birthdate)

@main_router.message(RegistrationStates.birthdate)
async def birthdate_handler(message: Message, state: FSMContext) -> None:
    birthdate=message.text
    user_data = await state.get_data()
    await state.clear()
    user = {
        "id": message.from_user.id,
        "name": user_data["name"],
        "phone_number": user_data["phone"],
        "city": user_data["city"],
        "jins": user_data["jins"],
        "birthdate": birthdate,
        "language": user_data["locale"]
    }
    await User().create(**user)
    await message.answer(f"{user_data["name"]} {text1}", reply_markup=main_menu())