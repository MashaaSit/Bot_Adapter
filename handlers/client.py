# КЛИЕНТСКАЯ ЧАСТЬ
from aiogram import types, Dispatcher

from Keyboards.client__kb import client_kb
from create_bot import bot
from Keyboards import client__kb
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в новый набор адаптеров! '
                                                 'Если ты еще не зарегестрирован, '
                                                 'напиши свои данные: ФИО(полностью), номер группы.', reply_markup=client_kb)
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])




