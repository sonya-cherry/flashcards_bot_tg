from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


""" Start keyboard"""
start_kb = InlineKeyboardMarkup()
ru_button = InlineKeyboardMarkup(text='Русский', callback_data='ru')
en_button = InlineKeyboardMarkup(text='English', callback_data='en')
start_kb.row(ru_button, en_button)


""" Basic keyboards """
base_kb_ru = InlineKeyboardMarkup()

help_button_ru = InlineKeyboardButton(text='Помощь', callback_data='help') # /help
repetition_button_ru = InlineKeyboardButton(text='Повторение', callback_data='begin_repetition') # /begin_repetition
add_button_ru = InlineKeyboardButton(text='Добавить карточку', callback_data='add') # /add
edit_kb_button_ru = InlineKeyboardButton(text='Настройки', callback_data='edit') # /edit

base_kb_ru.row(help_button_ru, repetition_button_ru)
base_kb_ru.row(edit_kb_button_ru, add_button_ru)


base_kb_en = InlineKeyboardMarkup()

help_button_en = InlineKeyboardButton(text='Help', callback_data='help') # /help
repetition_button_en = InlineKeyboardButton(text='Review', callback_data='begin_repetition') # /begin_repetition
add_button_en = InlineKeyboardButton(text='Add card', callback_data='add') # /add
edit_kb_button_en = InlineKeyboardButton(text='Settings', callback_data='edit') # /edit

base_kb_en.row(help_button_en, repetition_button_en)
base_kb_en.row(edit_kb_button_en, add_button_en)


""" Repetition keyboards """
next_kb_ru = InlineKeyboardMarkup()
next_button_ru = InlineKeyboardButton(text='Показать', callback_data='next') # /next
next_kb_ru.add(next_button_ru)

flip_kb_ru = InlineKeyboardMarkup()
flip_button_ru = InlineKeyboardButton(text='Перевернуть', callback_data='flip') # /flip
flip_kb_ru.add(flip_button_ru)


next_kb_en = InlineKeyboardMarkup()
next_button_en = InlineKeyboardButton(text='Show', callback_data='next') # /next
next_kb_en.add(next_button_en)

flip_kb_en = InlineKeyboardMarkup()
flip_button_en = InlineKeyboardButton(text='Flip', callback_data='flip') # /flip
flip_kb_en.add(flip_button_en)



""" Edit keyboards """
edit_kb_ru = InlineKeyboardMarkup()

delete_button_ru = InlineKeyboardButton('Удалить карточку', callback_data='delete_card') # /delete_card
hide_button_ru = InlineKeyboardButton('Спрятать карточку', callback_data='hide_card') # /hide_card
edit_button_ru = InlineKeyboardButton('Редактировать карточку', callback_data='edit_card') # /edit_card
send_list_button_ru = InlineKeyboardButton('Прислать список карточек', callback_data='list') # /list
language_button_ru = InlineKeyboardButton('Изменить язык', callback_data='change_language')
reminders_button_ru = InlineKeyboardButton('Напоминания', callback_data='reminders')
back_button_ru = InlineKeyboardButton('Назад в меню', callback_data='back')

edit_kb_ru.add(delete_button_ru)
edit_kb_ru.add(hide_button_ru)
edit_kb_ru.add(edit_button_ru)
edit_kb_ru.add(send_list_button_ru)
edit_kb_ru.add(language_button_ru)
edit_kb_ru.add(reminders_button_ru)
edit_kb_ru.add(back_button_ru)


edit_kb_en = InlineKeyboardMarkup()

delete_button_en = InlineKeyboardButton('Delete card', callback_data='delete_card') # /delete_card
hide_button_en = InlineKeyboardButton('Hide card', callback_data='hide_card') # /hide_card
edit_button_en = InlineKeyboardButton('Edit card', callback_data='edit_card') # /edit_card
send_list_button_en = InlineKeyboardButton('Send list of cards', callback_data='list') # /list
language_button_en = InlineKeyboardButton('Change language', callback_data='change_language')
reminders_button_en = InlineKeyboardButton('Reminders', callback_data='reminders')
back_button_en = InlineKeyboardButton('Back to menu', callback_data='back')

edit_kb_en.add(delete_button_en)
edit_kb_en.add(hide_button_en)
edit_kb_en.add(edit_button_en)
edit_kb_en.add(send_list_button_en)
edit_kb_en.add(language_button_en)
edit_kb_en.add(reminders_button_en)
edit_kb_en.add(back_button_en)


""" Edit card inline keyboards """
edit_front_kb_ru = InlineKeyboardMarkup()
edit_front_yes_button_ru = InlineKeyboardButton('Да', callback_data='yes_front')
edit_front_no_button_ru = InlineKeyboardButton('Нет', callback_data='no_front')
edit_front_kb_ru.add(edit_front_yes_button_ru, edit_front_no_button_ru)

edit_back_kb_ru = InlineKeyboardMarkup()
edit_back_yes_button_ru = InlineKeyboardButton('Да', callback_data='yes_back')
edit_back_no_button_ru = InlineKeyboardButton('Нет', callback_data='no_back')
edit_back_kb_ru.add(edit_back_yes_button_ru, edit_back_no_button_ru)

learn_again_kb_ru = InlineKeyboardMarkup()
learn_again_yes_button_ru = InlineKeyboardButton('Да', callback_data='yes_again')
learn_again_no_button_ru = InlineKeyboardButton('Нет', callback_data='no_again')
learn_again_kb_ru.add(learn_again_yes_button_ru, learn_again_no_button_ru)


edit_front_kb_en = InlineKeyboardMarkup()
edit_front_yes_button_en = InlineKeyboardButton('Yes', callback_data='yes_front')
edit_front_no_button_en = InlineKeyboardButton('No', callback_data='no_front')
edit_front_kb_en.add(edit_front_yes_button_en, edit_front_no_button_en)

edit_back_kb_en = InlineKeyboardMarkup()
edit_back_yes_button_en = InlineKeyboardButton('Yes', callback_data='yes_back')
edit_back_no_button_en = InlineKeyboardButton('No', callback_data='no_back')
edit_back_kb_en.add(edit_back_yes_button_en, edit_back_no_button_en)

learn_again_kb_en = InlineKeyboardMarkup()
learn_again_yes_button_en = InlineKeyboardButton('Yes', callback_data='yes_again')
learn_again_no_button_en = InlineKeyboardButton('No', callback_data='no_again')
learn_again_kb_en.add(learn_again_yes_button_en, learn_again_no_button_en)

"""  Other keyboards """

change_language_kb_ru = InlineKeyboardMarkup()
change_language_yes_button_ru = InlineKeyboardButton('Да', callback_data='yes_lang')
change_language_no_button_ru = InlineKeyboardButton('Нет', callback_data='no_lang')
change_language_kb_ru.add(change_language_yes_button_ru, change_language_no_button_ru)

change_language_kb_en = InlineKeyboardMarkup()
change_language_yes_button_en = InlineKeyboardButton('Yes', callback_data='yes_lang')
change_language_no_button_en = InlineKeyboardButton('No', callback_data='no_lang')
change_language_kb_en.add(change_language_yes_button_en, change_language_no_button_en)

