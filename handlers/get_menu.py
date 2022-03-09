from aiogram import types, Dispatcher
from create_bot import dp, bot


async def get_menu(message: types.Message):
    await message.answer('get_menu')


def register_handlers_get_menu(dp: Dispatcher):
    dp.register_message_handler(get_menu, commands=['get_menu'])