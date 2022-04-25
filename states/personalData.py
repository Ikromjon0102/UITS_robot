from aiogram.dispatcher.filters.state import StatesGroup,State

class PersonalData(StatesGroup):
    sname = State()
    name = State()
    byear = State()
    gender = State()
    social_status = State()
    course = State()
    phone = State()

class lotin(StatesGroup):
    Lotin2krill = State()
    krill2lotin = State()
