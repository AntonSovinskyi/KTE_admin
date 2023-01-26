from aiogram.utils import executor
from create_bot import dp
from handlers import admin, other
from data_base.postgres_db import connect

admin.register_handlers_admin(dp)
# other.register_handlers_other(dp)


async def on_startup(_):
    connect()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
