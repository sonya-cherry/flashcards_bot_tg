from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

# Creating bot objects
bot = Bot(token="6112328769:AAFd8CYRYtb-v05_bJFQahbDkUioBil_5Rw", parse_mode=ParseMode.HTML, timeout=60)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
