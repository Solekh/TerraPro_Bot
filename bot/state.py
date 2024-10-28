from aiogram.fsm.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    lang = State()
    phone = State()
    city = State()
    jins = State()
    name = State()
    birthdate = State()

