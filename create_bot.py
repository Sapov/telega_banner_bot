from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from token_bot import TOKEN
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

