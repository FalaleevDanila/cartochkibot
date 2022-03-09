from aiogram import types, Dispatcher
from create_bot import dp, bot


async def add_words(message: types.Message):
    await message.answer('add_words')


def register_handlers_add_words(dp: Dispatcher):
    dp.register_message_handler(add_words, commands=['add_words'])
