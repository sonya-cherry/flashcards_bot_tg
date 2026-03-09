from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from config import BOT_TOKEN

# Creating bot objects
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, timeout=60)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
