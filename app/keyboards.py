from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


"""  START KEYBOARD  """

start_kb = InlineKeyboardMarkup()
ru_button = InlineKeyboardButton(text="Русский", callback_data="ru")
en_button = InlineKeyboardButton(text="English", callback_data="en")
start_kb.row(ru_button, en_button)


"""  MAIN MENU KEYBOARD  """

base_kb_ru = InlineKeyboardMarkup()
help_button_ru = InlineKeyboardButton(text="Помощь", callback_data="help")
repetition_button_ru = InlineKeyboardButton(text="Повторение", callback_data="begin_repetition")
add_button_ru = InlineKeyboardButton(text="Добавить карточку", callback_data="add")
edit_kb_button_ru = InlineKeyboardButton(text="Настройки", callback_data="edit")
base_kb_ru.row(help_button_ru, repetition_button_ru)
base_kb_ru.row(edit_kb_button_ru, add_button_ru)

base_kb_en = InlineKeyboardMarkup()
help_button_en = InlineKeyboardButton(text="Help", callback_data="help")
repetition_button_en = InlineKeyboardButton(text="Review", callback_data="begin_repetition")
add_button_en = InlineKeyboardButton(text="Add card", callback_data="add")
edit_kb_button_en = InlineKeyboardButton(text="Settings", callback_data="edit")
base_kb_en.row(help_button_en, repetition_button_en)
base_kb_en.row(edit_kb_button_en, add_button_en)


"""  REPETITION KEYBOARDS  """

next_kb_ru = InlineKeyboardMarkup()
next_button_ru = InlineKeyboardButton(text="Показать", callback_data="next")
next_kb_ru.add(next_button_ru)

flip_kb_ru = InlineKeyboardMarkup()
flip_button_ru = InlineKeyboardButton(text="Перевернуть", callback_data="flip")
flip_kb_ru.add(flip_button_ru)

next_kb_en = InlineKeyboardMarkup()
next_button_en = InlineKeyboardButton(text="Show", callback_data="next")
next_kb_en.add(next_button_en)

flip_kb_en = InlineKeyboardMarkup()
flip_button_en = InlineKeyboardButton(text="Flip", callback_data="flip")
flip_kb_en.add(flip_button_en)


"""  SETTINGS  """

edit_kb_ru = InlineKeyboardMarkup()
delete_button_ru = InlineKeyboardButton(text="Удалить карточку", callback_data="delete_card")
hide_button_ru = InlineKeyboardButton(text="Спрятать карточку", callback_data="hide_card")
edit_button_ru = InlineKeyboardButton(text="Редактировать карточку", callback_data="edit_card")
send_list_button_ru = InlineKeyboardButton(text="Прислать список карточек", callback_data="list")
language_button_ru = InlineKeyboardButton(text="Изменить язык", callback_data="change_language")
reminders_button_ru = InlineKeyboardButton(text="Напоминания", callback_data="reminders")
back_button_ru = InlineKeyboardButton(text="Назад в меню", callback_data="back")

edit_kb_ru.add(delete_button_ru)
edit_kb_ru.add(hide_button_ru)
edit_kb_ru.add(edit_button_ru)
edit_kb_ru.add(send_list_button_ru)
edit_kb_ru.add(language_button_ru)
edit_kb_ru.add(reminders_button_ru)
edit_kb_ru.add(back_button_ru)

edit_kb_en = InlineKeyboardMarkup()
delete_button_en = InlineKeyboardButton(text="Delete card", callback_data="delete_card")
hide_button_en = InlineKeyboardButton(text="Hide card", callback_data="hide_card")
edit_button_en = InlineKeyboardButton(text="Edit card", callback_data="edit_card")
send_list_button_en = InlineKeyboardButton(text="Send list of cards", callback_data="list")
language_button_en = InlineKeyboardButton(text="Change language", callback_data="change_language")
reminders_button_en = InlineKeyboardButton(text="Reminders", callback_data="reminders")
back_button_en = InlineKeyboardButton(text="Back to menu", callback_data="back")

edit_kb_en.add(delete_button_en)
edit_kb_en.add(hide_button_en)
edit_kb_en.add(edit_button_en)
edit_kb_en.add(send_list_button_en)
edit_kb_en.add(language_button_en)
edit_kb_en.add(reminders_button_en)
edit_kb_en.add(back_button_en)


"""  EDIT CARD KEYBOARD  """

edit_front_kb_ru = InlineKeyboardMarkup()
edit_front_yes_button_ru = InlineKeyboardButton(text="Да", callback_data="yes_front")
edit_front_no_button_ru = InlineKeyboardButton(text="Нет", callback_data="no_front")
edit_front_kb_ru.add(edit_front_yes_button_ru, edit_front_no_button_ru)

edit_back_kb_ru = InlineKeyboardMarkup()
edit_back_yes_button_ru = InlineKeyboardButton(text="Да", callback_data="yes_back")
edit_back_no_button_ru = InlineKeyboardButton(text="Нет", callback_data="no_back")
edit_back_kb_ru.add(edit_back_yes_button_ru, edit_back_no_button_ru)

learn_again_kb_ru = InlineKeyboardMarkup()
learn_again_yes_button_ru = InlineKeyboardButton(text="Да", callback_data="yes_again")
learn_again_no_button_ru = InlineKeyboardButton(text="Нет", callback_data="no_again")
learn_again_kb_ru.add(learn_again_yes_button_ru, learn_again_no_button_ru)

edit_front_kb_en = InlineKeyboardMarkup()
edit_front_yes_button_en = InlineKeyboardButton(text="Yes", callback_data="yes_front")
edit_front_no_button_en = InlineKeyboardButton(text="No", callback_data="no_front")
edit_front_kb_en.add(edit_front_yes_button_en, edit_front_no_button_en)

edit_back_kb_en = InlineKeyboardMarkup()
edit_back_yes_button_en = InlineKeyboardButton(text="Yes", callback_data="yes_back")
edit_back_no_button_en = InlineKeyboardButton(text="No", callback_data="no_back")
edit_back_kb_en.add(edit_back_yes_button_en, edit_back_no_button_en)

learn_again_kb_en = InlineKeyboardMarkup()
learn_again_yes_button_en = InlineKeyboardButton(text="Yes", callback_data="yes_again")
learn_again_no_button_en = InlineKeyboardButton(text="No", callback_data="no_again")
learn_again_kb_en.add(learn_again_yes_button_en, learn_again_no_button_en)


"""  LANGUAGE KEYBOARDS  """

change_language_kb_ru = InlineKeyboardMarkup()
change_language_yes_button_ru = InlineKeyboardButton(text="Да", callback_data="yes_lang")
change_language_no_button_ru = InlineKeyboardButton(text="Нет", callback_data="no_lang")
change_language_kb_ru.add(change_language_yes_button_ru, change_language_no_button_ru)

change_language_kb_en = InlineKeyboardMarkup()
change_language_yes_button_en = InlineKeyboardButton(text="Yes", callback_data="yes_lang")
change_language_no_button_en = InlineKeyboardButton(text="No", callback_data="no_lang")
change_language_kb_en.add(change_language_yes_button_en, change_language_no_button_en)


"""  REMINDERS KEYBOARDS  """

reminders_kb_ru = InlineKeyboardMarkup(row_width=2)
reminders_enable_button_ru = InlineKeyboardButton("Включить", callback_data="reminder_enable")
reminders_disable_button_ru = InlineKeyboardButton("Выключить", callback_data="reminder_disable")
reminders_set_hour_button_ru = InlineKeyboardButton("Выбрать час", callback_data="reminder_choose_hour")
reminders_back_button_ru = InlineKeyboardButton("Назад", callback_data="reminders_back")
reminders_kb_ru.add(reminders_enable_button_ru, reminders_disable_button_ru)
reminders_kb_ru.add(reminders_set_hour_button_ru)
reminders_kb_ru.add(reminders_back_button_ru)

reminders_kb_en = InlineKeyboardMarkup(row_width=2)
reminders_enable_button_en = InlineKeyboardButton("Enable", callback_data="reminder_enable")
reminders_disable_button_en = InlineKeyboardButton("Disable", callback_data="reminder_disable")
reminders_set_hour_button_en = InlineKeyboardButton("Choose hour", callback_data="reminder_choose_hour")
reminders_back_button_en = InlineKeyboardButton("Back", callback_data="reminders_back")
reminders_kb_en.add(reminders_enable_button_en, reminders_disable_button_en)
reminders_kb_en.add(reminders_set_hour_button_en)
reminders_kb_en.add(reminders_back_button_en)


reminder_hours_kb = InlineKeyboardMarkup(row_width=4)
for hour in [8, 10, 12, 14, 16, 18, 20, 22]:
    reminder_hours_kb.insert(
        InlineKeyboardButton(text=f"{hour}:00", callback_data=f"reminder_hour_{hour}")
    )
