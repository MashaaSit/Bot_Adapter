from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/NOTIFICATION')
b2 = KeyboardButton('/MEDIA')
b3 = KeyboardButton('/MAILING')

client_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

client_kb.row(b1,b2,b3)
#
# add(b1).add(b2).insert(b3)
# add(b3)
