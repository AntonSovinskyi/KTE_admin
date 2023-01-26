# from aiogram import types, Dispatcher
# from create_bot import admin_id, bot
# from keyboards.admin_kb import *
# from data_base.postgres_db import *
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher.filters import Text
#
#
# # class FSMadmin(StatesGroup):
# #     dj = State()
# #     time = State()
# #     price = State()
# #     address = State()
# #     day = State()
#
#
# # Launch the section for changing information in the database
# # @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer('Оберіть захід, в який бажаєте внести зміни', reply_markup=table_button_admin)
#
#
# # Selecting event
# # @dp.message_handler(commands=['Milonga'])
# async def milonga(message: types.Message):
#     await bot.send_message(message.from_user.id, "Оберіть інформацію, яку бажаєте змінити", reply_markup=milonga_table_change)
#
#
# # Selecting event
# # @dp.message_handler(commands=['Practice'])
# async def practice(message: types.Message):
#     await bot.send_message(message.from_user.id, "Оберіть інформацію, яку бажаєте змінити", reply_markup=practice_table_change)
#
#
# # Selecting event
# # @dp.message_handler(commands=['Lessons'])
# async def lessons(message: types.Message):
#     await bot.send_message(message.from_user.id, "Натисніть кнопку", reply_markup=lessons_table_change)
#
#
# # Selecting row to change
# async def milonga_changes(message: types.Message):
#     text_row = message.text
#     if text_row == 'Dj':
#         await bot.send_message(message.from_user.id, "Введіть им'я, без вказання літер 'dj'")  # reply_markup=day_button_change)
#     if text_row == 'Час':
#         await bot.send_message(message.from_user.id, "Введіть час в форматі: 14:00 - 15:00")
#     if text_row == 'Ціна':
#         await bot.send_message(message.from_user.id, "Введіть ціну в форматі: 150 грн")
#
#
#     # async def practice_address_change(message: types.Message):
# #     prac_address_row = message.text  # .lstrip('/')
# #     if prac_address_row == 'Адреса':
# #         await bot.send_message(message.from_user.id, "Введіть им'я dj")  # reply_markup=day_button_change)
#
# dj = None
# print(f"glob_dj = {dj}")
#
#
# # Entering new data
# async def dj_name(message: types.Message):
#     global dj
#     dj = message.text
#     print(f"local_dj = {dj}")
#     await bot.send_message(message.from_user.id, 'Оберіть день тижня', reply_markup=day_button_change)  # milonga_change_dj_sql(dj))
#
#
# # Selecting day to change row
# async def choose_day(message: types.Message):
#     print(f"glob_dj_new = {dj}")
#     day_of_the_week = ["Понеділок", "Вівторок", "Середа", "Четверг", "П'ятниця", "Субота", "Неділя"]
#     day = message.text
#     print(day)
#     if day in day_of_the_week:
#         await bot.send_message(message.from_user.id, 'Dj змінено', milonga_change_dj_sql(dj, day))
#     else:
#         await bot.send_message(message.from_user.id, 'Невідома команда')
#
#
# # Register handlers
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(start, commands=['start'])  # state=None)
#     dp.register_message_handler(milonga, Text('Мілонга'))
#     dp.register_message_handler(practice, Text('Практика'))
#     dp.register_message_handler(lessons, Text('Уроки'))
#     dp.register_message_handler(milonga_changes, Text(['Dj', 'Час', 'Ціна']))
#     dp.register_message_handler(dj_name)
#     dp.register_message_handler(choose_day, Text(equals=["Понеділок", "Вівторок", "Середа", "Четверг", "П'ятниця", "Субота", "Неділя"]))
#
