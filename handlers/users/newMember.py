import logging
from data.spsheeds import sheet
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from data.dates import genderdata,status,courses
from aiogram.dispatcher.filters import Regexp

from keyboards.inline.genKey import genderKey, answerKey
from keyboards.inline.kursKey import proKey
from keyboards.inline.s_status import s_statusKey
from keyboards.inline.yesno import answer_callback
from loader import dp
from states.personalData import PersonalData

PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
DATA_REGEX = r"(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"



@dp.message_handler(content_types='contact',is_sender_contact=True)
async def enter_test(msg: types.Message,state:FSMContext):
    await msg.answer("Familiyangizni kiriting\nExample: <b>Valiyev</b>",
                     reply_markup=ReplyKeyboardRemove())
    phone = msg.contact.phone_number
    await state.update_data(
        {'phone': phone}
    )
    # logging.info(msg)
    await PersonalData.sname.set()

@dp.message_handler(state=PersonalData.sname)
async def enter_name(msg: types.Message, state:FSMContext):
    sname = msg.text
    await state.update_data(
        {'sname':sname}
    )
    await msg.answer("Ismingizni kiriting\nExample: <b>Alijon</b>")
    await PersonalData.name.set()



@dp.message_handler(state=PersonalData.name)
async def enter_name(msg: types.Message, state:FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )

    await msg.answer(f"<b>{name.capitalize()},</b> telefon nomeriz telegramdagi "
                     f"nomer bilan bilan bir xilmi?",reply_markup=answerKey)

@dp.callback_query_handler(answer_callback.filter(),state=PersonalData.name)
async def answ(call: types.CallbackQuery):
    await call.message.delete()
    javob = call.data
    logging.info(javob)
    if javob == "answer:yes":
        await call.message.answer("Tug'ilgan kuningizni kiriting\n"
        "Example: <b>15.12.1999</b> ")
        await PersonalData.byear.set()
    elif javob == "answer:no":
        await call.message.answer("Siz bilan bog'lanish uchun telefon raqamingizni kiriting\n"
                                  "Exapmle: <b>98 765 4321</b>  ")
        await PersonalData.phone.set()
    await call.answer(cache_time=60)

@dp.message_handler(state=PersonalData.phone)
async def answ(msg: types.Message,state:FSMContext):
    phone = msg.text
    await state.update_data({'phone': phone})
    await msg.answer("Tug'ilgan kuningizni kiriting\n"
                  "Example: <b>15.12.1999</b> ")
    await PersonalData.byear.set()
    # logging.info(msg)
    # else:
    #     await msg.answer("Telefon raqam formati to'g'ri kelmadi\n"
    #                               "Exapmle: <b>98 765 4321</b>  ")
    #     await PersonalData.phone.set()

@dp.message_handler(state=PersonalData.byear)
async def enter_name(msg: types.Message, state:FSMContext):
    byear = msg.text
    await state.update_data({'byear':byear})
    await msg.answer("Jinsingiz",reply_markup=genderKey)
    await PersonalData.gender.set()
    # else:
    #     await msg.answer("Tu'g'ilgan kun formati to'g'ri kelmadi\n"
    #                               "Exapmle: <b>98 765 4321</b>")
    #     await PersonalData.byear.set()

@dp.callback_query_handler(state=PersonalData.gender)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    cal = call.data
    await state.update_data(
        {'gender':cal}
    )
    await call.message.delete()
    await call.message.answer("Ijtimoiy holatingiz",
                              reply_markup=s_statusKey)
    await PersonalData.next()

@dp.callback_query_handler(state=PersonalData.social_status)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    s_status = call.data
    await call.message.delete()
    await state.update_data(
        {'status':s_status}
    )
    await call.message.answer("Kurslardan birini tanlang",
                              reply_markup=proKey)
    await PersonalData.next()
@dp.callback_query_handler(state=PersonalData.course)
async def enter_name(call: types.CallbackQuery, state:FSMContext):
    course = call.data
    await call.message.delete()
    await state.update_data(
        {'course':course}
    )

    # ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    sname = data.get('sname')
    name = data.get('name')
    byear = data.get('byear')
    gender = genderdata.get(data.get('gender'))
    s_status = status.get(data.get('status'))
    course = courses.get(data.get('course'))
    phone = data.get('phone')
    id = call.from_user.id


    xabar = "Quyidagi ma'lumotlar qabul qilindi:\n"
    xabar += f"Ismingiz - {name.capitalize()}\n"
    xabar += f"Familiyangiz - {sname.capitalize()}\n"
    xabar += f"Jinsingiz - {gender}\n"
    xabar += f"Tug'ilgan yilingiz - {byear}\n"
    xabar += f"Telefon - {phone}\n"
    xabar += f"Ijtimoiy holatingiz - {s_status}\n"
    xabar += f"Tanlagan kursingiz - {course}\n"
    newmember = [id,sname.capitalize(),name.capitalize(),
                 gender,byear,phone, s_status,course]
    sheet.append_row(newmember)
    await call.message.answer(xabar)


    msg = f"<b>Yangi o'quvchi</b>\n"
    msg += f"Ismi - {name.capitalize()}\n"
    msg += f"Familiya - {sname.capitalize()}\n"
    msg += f"Telefon - {phone}\n"
    msg += f"Tanlagan kursi - {course}\n"
    if course=="Python":
        await dp.bot.send_message(92473435, msg)
    elif course=="Web dasturlash":
        await dp.bot.send_message(1837827627, msg)
    elif course=="Kompyuter savodxonligi":
        await dp.bot.send_message(1009831331, msg)
    await state.finish()
    # await state.reset_state(with_data=False)