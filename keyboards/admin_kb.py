from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Admin keyboard buttons
table_button1 = KeyboardButton('Мілонга')
table_button2 = KeyboardButton('Практика')
table_button3 = KeyboardButton('Уроки')


# Writing the format for displaying menu buttons
table_button_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(table_button1, table_button2, table_button3)


milonga_table1 = KeyboardButton('Dj')
milonga_table2 = KeyboardButton('Час')
milonga_table3 = KeyboardButton('Ціна')


# Writing the format for displaying menu buttons
milonga_table_change = ReplyKeyboardMarkup(resize_keyboard=True).row(milonga_table1, milonga_table2, milonga_table3)


practice_table1 = KeyboardButton('Час')
practice_table2 = KeyboardButton('Ціна')
practice_table3 = KeyboardButton('Адреса')


# Writing the format for displaying menu buttons
practice_table_change = ReplyKeyboardMarkup(resize_keyboard=True).row(practice_table1, practice_table2, practice_table3)


lessons_table1 = KeyboardButton('Ціна')


# Writing the format for displaying menu buttons
lessons_table_change = ReplyKeyboardMarkup(resize_keyboard=True).add(lessons_table1)

day_button1 = KeyboardButton('Понеділок')
day_button2 = KeyboardButton('Вівторок')
day_button3 = KeyboardButton('Середа')
day_button4 = KeyboardButton('Четвер')
day_button5 = KeyboardButton("П'ятниця")
day_button6 = KeyboardButton('Субота')
day_button7 = KeyboardButton('Неділя')


# Writing the format for displaying menu buttons
day_button_change = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True

day_button_change.row(day_button1, day_button2).row(day_button3, day_button4).\
                    row(day_button5, day_button6).add(day_button7)
