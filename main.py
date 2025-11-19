import logging
from aiogram.utils import executor
from bot import dp
from handlers import *
import schedule
import asyncio
import time

# logging configuration
logging.basicConfig(level=logging.INFO)

# handler registration
dp.register_message_handler(start_message, commands=['start'])
dp.register_callback_query_handler(greeting, lambda query: query.data == 'ru' or query.data == 'en', state=SetLanguage.GET_LANGUAGE)
dp.register_callback_query_handler(help, lambda query: query.data == 'help')
dp.register_callback_query_handler(back_to_menu, lambda query: query.data == 'back')

dp.register_callback_query_handler(add_card, lambda query: query.data == 'add')
dp.register_message_handler(add_card_front_side, state=AddCard.ADD_FRONT)
dp.register_message_handler(add_card_back_side, state=AddCard.ADD_BACK)

dp.register_callback_query_handler(edit, lambda query: query.data == 'edit')

dp.register_callback_query_handler(ask_if_change_language, lambda query: query.data == 'change_language')
dp.register_callback_query_handler(change_language, lambda query: query.data == 'yes_lang' or  query.data == 'no_lang', state=ChangeLanguage.GET_CONFIRMATION)

dp.register_callback_query_handler(send_list, lambda query: query.data == 'list')

dp.register_callback_query_handler(delete_card, lambda query: query.data == 'delete_card')
dp.register_message_handler(delete_state, state=DeleteCard.GET_ID)

dp.register_callback_query_handler(hide_card, lambda query: query.data == 'hide_card')
dp.register_message_handler(hide_state, state=HideCard.HIDE)

dp.register_callback_query_handler(edit_card, lambda query: query.data == 'edit_card')
dp.register_message_handler(ask_if_edit_front, state=EditCard.GET_ID)
dp.register_callback_query_handler(wait_for_front, lambda query: query.data == 'yes_front', state=EditCard.GET_ID)
dp.register_message_handler(edit_front, state=EditCard.EDIT_FRONT)
dp.register_callback_query_handler(ask_if_edit_back, lambda query: query.data == 'no_front', state=EditCard.GET_ID)
dp.register_callback_query_handler(wait_for_back, lambda query: query.data == 'yes_back', state=EditCard.ASK_IF_EDIT_BACK)
dp.register_message_handler(edit_back, state=EditCard.EDIT_BACK)
dp.register_callback_query_handler(ask_if_learn_again, lambda query: query.data == 'no_back', state=EditCard.ASK_IF_EDIT_BACK)
dp.register_callback_query_handler(learn_again, lambda query: query.data == 'no_again' or query.data == 'yes_again', state=EditCard.LEARN_AGAIN)

dp.register_callback_query_handler(begin_repetition, lambda query: query.data == 'begin_repetition')
dp.register_callback_query_handler(show_front, lambda query: query.data == 'next', state=ShowCard.NEXT)
dp.register_callback_query_handler(show_back, lambda query: query.data == 'flip', state=ShowCard.FLIP)


@dp.errors_handler(exception=Exception)
async def handle_exception(update, exception):
    chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id
    await bot.send_message(chat_id, "Oops! Something went wrong. Please try again later.\nУпс! Что-то пошло не так. Попробуйте заново позже.")
    logging.exception(f"Exception occurred for chat_id={chat_id}:\n{exception}")


schedule.every().day.at("15:30").do(db_reschedule_cards)

async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == '__main__':
    from aiogram import executor
    from aiogram import types

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())

    executor.start_polling(dp, skip_updates=True)
    loop.run_until_complete(dp.shutdown())
    loop.run_until_complete(dp.storage.close())
    loop.close()
