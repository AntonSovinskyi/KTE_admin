# from aiogram import types, Dispatcher
# from create_bot import admin_id, bot
# from keyboards.admin_kb import *
# from data_base.postgres_db import *
# from aiogram.dispatcher.filters import Text
#
#
# day = None
# info = None
#
#
# # Launch the section for changing information in the database
# # @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer('Оберіть захід, в який бажаєте внести зміни', reply_markup=table_button_admin)
#
#
# # Selecting event
# # @dp.message_handler(Text(['Мілонга', 'Практика', 'Уроки']))
# async def choose_event(message: types.Message):
#     text_row = message.text
#     if text_row == 'Мілонга':
#         await bot.send_message(message.from_user.id, 'Оберіть день тижня', reply_markup=day_button_change)
#     elif text_row == 'Практика':
#         await bot.send_message(message.from_user.id, 'Оберіть день тижня', reply_markup=day_button_change)
#     elif text_row == 'Уроки':
#         await bot.send_message(message.from_user.id, 'Оберіть день тижня', reply_markup=day_button_change)
#
#
# # Selecting event
# # @dp.message_handler(commands=['Practice'])
# async def practice(message: types.Message):
#     await bot.send_message(message.from_user.id, "Оберіть інформацію, яку бажаєте змінити",
#                            reply_markup=practice_table_change)
#
#
# # Selecting event
# # @dp.message_handler(commands=['Lessons'])
# async def lessons(message: types.Message):
#     await bot.send_message(message.from_user.id, "Натисніть кнопку", reply_markup=lessons_table_change)
#
#
# async def choose_day(message: types.Message):
#     global day
#     day_of_the_week = ["Понеділок", "Вівторок", "Середа", "Четверг", "П'ятниця", "Субота", "Неділя"]
#     day = message.text
#     print(f'Day: {day}')
#     if day in day_of_the_week:
#         await bot.send_message(message.from_user.id, "Оберіть інформацію, яку бажаєте змінити",
#                                reply_markup=milonga_table_change)
#
#
# # Entering new data
# async def given_info(message: types.Message):
#     global info
#     info = message.text
#     if info == 'Dj':
#         await bot.send_message(message.from_user.id, "Введіть ім'я без вказання літер 'dj'")  # reply_markup=day_button_change)
#     elif info == 'Час':
#         await bot.send_message(message.from_user.id, "Введіть час в форматі: 14:00 - 15:00")
#     elif info == 'Ціна':
#         await bot.send_message(message.from_user.id, "Введіть ціну в форматі: 150 грн")
#
#
# # Selecting day to change row
# async def info_update(message: types.Message):
#     new_data = message.text
#     if info == 'Dj':
#         await bot.send_message(message.from_user.id, 'Dj змінено', milonga_change_dj_sql(new_data, day))
#     elif info == 'Час':
#         await bot.send_message(message.from_user.id, 'Час змінено', milonga_change_time_sql(new_data, day))
#     elif info == 'Ціна':
#         await bot.send_message(message.from_user.id, 'Ціну змінено', milonga_change_price_sql(new_data, day))
#     else:
#         await bot.send_message(message.from_user.id, 'Невідома команда')
#
#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(start, commands=['start'])  # state=None)
#     dp.register_message_handler(choose_event, Text(['Мілонга', 'Практика', 'Уроки']))
#     dp.register_message_handler(practice, Text('Практика'))
#     dp.register_message_handler(lessons, Text('Уроки'))
#     dp.register_message_handler(choose_day, Text(equals=(["Понеділок", "Вівторок",
#                                                           "Середа", "Четверг", "П'ятниця", "Субота", "Неділя"])))
#     # dp.register_message_handler(milonga, Text('Мілонга'))
#     dp.register_message_handler(given_info, Text(['Dj', 'Час', 'Ціна']))
#     dp.register_message_handler(info_update)
#