from aiogram.utils import executor
from create_bot import dp


async def starting(_):
    print('Starting ... ')

from handlers import add_words, get_menu, start_test

add_words.register_handlers_add_words(dp)
get_menu.register_handlers_get_menu(dp)
start_test.register_handlers_start_test(dp)

executor.start_polling(dp, skip_updates=True, on_startup=starting)
