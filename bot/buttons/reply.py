from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def registration_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Share Phone number", request_contact=True),
    ])
    rkb.adjust(1, 1)
    return rkb.as_markup(resize_keyboard=True)


def main_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="💳 Моя дисконтная карта"),
        KeyboardButton(text="🛍 Заказать на сайте"),
        KeyboardButton(text="⚙️ Настройки"),
        KeyboardButton(text="📍 Наши магазины"),
        KeyboardButton(text="☎️ Связаться с нами"),
        KeyboardButton(text="✍️ Оставить отзыв"),
        KeyboardButton(text="💼 Вакансии"),
        KeyboardButton(text="🔄 Условия возврата/обмена"),
    ])
    rkb.adjust(1, 1, 2, 2, 2)
    return rkb.as_markup(resize_keyboard=True)

def lang():
    rkb =  ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text = "Русский 🇷🇺"),
        KeyboardButton(text = "O'zbek 🇺🇿")
    ])
    return rkb.as_markup()


def cities():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text = "Buxoro"),
        KeyboardButton(text = "Tashkent"),
        KeyboardButton(text = "Samarqand"),
        KeyboardButton(text = "Farg'ona"),
        KeyboardButton(text = "Andijon"),
        KeyboardButton(text = "Namangan"),
    ])
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True)

def jins():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text = "👨‍ Мужской"),
        KeyboardButton(text = "👩‍ Женский"),
    ])
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True, one_time=True)