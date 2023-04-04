from aiogram import Bot
from aiogram.dispatcher import Dispatcher

TOKEN = '5948835614:AAHkb6OLH52yklEmy2DT5oNttfcOfRK5r0Y'

from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)