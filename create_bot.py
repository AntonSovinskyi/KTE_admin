from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import logging


API_TOKEN = '5641897666:AAEPhICr4UlRt8SZzpl9Mgd6oFRya_WouD4'
admin_id = ['311330375']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
