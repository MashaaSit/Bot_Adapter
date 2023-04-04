from aiogram.dspatcher import FSMContext
from aiogram.dspatcher.filters.state import State, StatesGroup

class FSMAdmin (StatesGroup):
    photo = State()
    name  = State

#
@dp.message_handler(commands='upload', state=None)
async def cm_start(message: types.Message):
