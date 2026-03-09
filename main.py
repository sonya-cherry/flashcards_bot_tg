import logging
import schedule
import asyncio
from datetime import datetime

from aiogram.utils import executor

from app.bot import dp, bot
from db.db import db_reschedule_cards, db_create_table
from app.handlers import *
from app.states import *


# logging configuration
logging.basicConfig(level=logging.INFO)

# handler registration
dp.register_message_handler(start_message, commands=['start'])
dp.register_callback_query_handler(greeting, lambda query: query.data == 'ru' or query.data == 'en', state=SetLanguage.GET_LANGUAGE)
dp.register_callback_query_handler(show_help, lambda query: query.data == 'help')
dp.register_message_handler(help_command, commands=['help'])
dp.register_callback_query_handler(back_to_menu, lambda query: query.data == 'back')

dp.register_callback_query_handler(add_card, lambda query: query.data == 'add')
dp.register_message_handler(add_card_front_side, state=AddCard.ADD_FRONT)
dp.register_message_handler(add_card_back_side, state=AddCard.ADD_BACK)

dp.register_callback_query_handler(settings, lambda query: query.data == 'edit')

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

dp.register_callback_query_handler(open_reminders_settings, lambda query: query.data == 'reminders')
dp.register_callback_query_handler(enable_reminders, lambda query: query.data == 'reminder_enable', state=ReminderSettings.CHOOSING)
dp.register_callback_query_handler(disable_reminders, lambda query: query.data == 'reminder_disable', state=ReminderSettings.CHOOSING)
dp.register_callback_query_handler(choose_reminder_hour, lambda query: query.data == 'reminder_choose_hour', state=ReminderSettings.CHOOSING)
dp.register_callback_query_handler(set_reminder_hour, lambda query: query.data.startswith('reminder_hour_'), state=ReminderSettings.CHOOSING)
dp.register_callback_query_handler(back_to_settings_from_reminders, lambda query: query.data == 'reminders_back',state=ReminderSettings.CHOOSING)

@dp.errors_handler(exception=Exception)
async def handle_exception(update, exception):
    chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id
    await bot.send_message(chat_id, "Oops! Something went wrong. Please try again later.\nУпс! Что-то пошло не так. Попробуйте заново позже.")
    logging.exception(f"Exception occurred for chat_id={chat_id}:\n{exception}")


schedule.every().day.at("23:59").do(db_reschedule_cards)

last_reminder_check = None   
async def scheduler():
    global last_reminder_check

    while True:
        schedule.run_pending()

        now = datetime.now()
        current_slot = (now.date(), now.hour, now.minute)

        if now.minute == 0 and last_reminder_check != current_slot:
            await send_reminders_for_hour(now.hour)
            last_reminder_check = current_slot

        await asyncio.sleep(30)

if __name__ == '__main__':
    db_create_table()

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())

    executor.start_polling(dp, skip_updates=True)
    loop.close()
