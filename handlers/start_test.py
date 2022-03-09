from aiogram import types, Dispatcher
from create_bot import dp, bot


async def start_test(message: types.Message):
    await message.answer('start_test')


def register_handlers_start_test(dp: Dispatcher):
    dp.register_message_handler(start_test, commands=['start_test'])