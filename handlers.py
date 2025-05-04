from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, InputFile
from db import *
from keyboards import *
from bot import bot
from io import BytesIO
import json

# loading messages templates according to the given language (ru/en)
def load_text(language):
   with open(f'{language}.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# returns the needed message text in users language
def get_text(key, user_id):
    language = db_get_language(user_id)
    texts = load_text(language)
    return texts.get(key)


class SetLanguage(StatesGroup):
    GET_LANGUAGE = State()


# /start
async def start_message(callback_query : CallbackQuery, state:FSMContext):
    await SetLanguage.GET_LANGUAGE.set()
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, 'Выберите язык: / Choose the language:', reply_markup=start_kb)


async def greeting(callback_query : CallbackQuery, state:FSMContext):
    user_id = callback_query.from_user.id
    if callback_query.data == 'ru': # russian = 1, english = 0
        db_set_language(user_id, 1)
        await bot.send_message(user_id, get_text('start-msg', user_id), reply_markup=base_kb_ru)
    else:
        db_set_language(user_id, 0)
        await bot.send_message(user_id, get_text('start-msg', user_id), reply_markup=base_kb_en)
        
    await state.finish()


# /help
async def help(callback_query : CallbackQuery):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await bot.send_message(user_id, get_text('help-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # help-msg
 
# /edit
async def edit(callback_query : CallbackQuery):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await bot.send_message(user_id, get_text('settings-msg', user_id), reply_markup=edit_kb_ru if lang == 'ru' else edit_kb_en) # settings-msg


async def reminders(callback_query : CallbackQuery):
    pass


async def back_to_menu(callback_query : CallbackQuery):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)

    await bot.send_message(user_id, get_text('back-to-menu-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en)


"""  CHANGE LANGUAGE  """

class ChangeLanguage(StatesGroup):
    GET_CONFIRMATION = State()


async def ask_if_change_language(callback_query : CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await ChangeLanguage.GET_CONFIRMATION.set()
    await bot.send_message(user_id, get_text('change-language-msg', user_id), reply_markup=change_language_kb_ru if lang == 'ru' else change_language_kb_en)


async def change_language(callback_query : CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    if callback_query.data == 'yes_lang':
        db_change_language(user_id)
        lang = db_get_language(user_id)
        await bot.send_message(user_id, get_text('language-is-changed-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en)
    elif callback_query.data == 'no_lang':
        lang = db_get_language(user_id)
        await bot.send_message(user_id, get_text('language-stays-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en)
    await state.finish()


"""  ADDING NEW FLASHCARD  """

class AddCard(StatesGroup):
    ADD_FRONT = State()
    ADD_BACK = State()

# /add
async def add_card(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    # switching to FRONT
    await bot.send_message(user_id, get_text('add-card-msg', user_id)) # add-card-msg
    await AddCard.ADD_FRONT.set()


# handler adding front side
async def add_card_front_side(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(front=message.text)
    await message.answer(get_text('add-card-back-msg', user_id)) # add-card-back-msg
    await AddCard.ADD_BACK.set()


# handler adding back side
async def add_card_back_side(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = db_get_language(user_id)
    async with state.proxy() as data:
        # saving card in db 
        data['back'] = message.text
        db_add_card(user_id, data['front'], data['back'])

    # returnung to neutral state
    await state.finish()
    await message.answer(get_text('add-card-is-saved-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # add-card-is-saved-msg


"""  SENDING THE LIST OF FLASHCARDS  """

# /list
async def send_list(callback_query : CallbackQuery):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await bot.send_message(user_id, get_text('send-list-msg', user_id)) #send-list-msg
    
    bio = BytesIO()

    data = db_get_user_cards(user_id)
    for line in data:
        bio.write(' | '.join(map(str, line)).encode('utf-8') + b'\n')
    bio.seek(0)

    await bot.send_document(callback_query.message.chat.id, InputFile(bio, filename='flashcards.txt'), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en)


""" DELETE """

class DeleteCard(StatesGroup):
    GET_ID = State()


# /delete, deletes the flashcard according to its id (user gets the id from the card list)
async def delete_card(callback_query : CallbackQuery, state: FSMContext):
    await DeleteCard.GET_ID.set()

    user_id = callback_query.from_user.id
    await bot.send_message(user_id, get_text('delete-card-which-one-msg', user_id)) # delete-card-which-one-msg

    bio = BytesIO()
    
    flashcards = db_get_user_cards(user_id)
    await state.update_data(card_ids=[x[0] for x in flashcards])
    for line in flashcards:
        bio.write(' | '.join(map(str, line)).encode('utf-8') + b'\n')
    bio.seek(0)

    await bot.send_document(callback_query.message.chat.id, InputFile(bio, filename='flashcards.txt'))


# waits for the id
async def delete_state(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = db_get_language(user_id)
    card_id = message.text
    data = await state.get_data()
    if card_id.isnumeric() and int(card_id) in data['card_ids']:
        print(0)
        db_delete_card(card_id)
        await message.answer(get_text('delete-card-is-deleted-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # delete-card-is-deleted
    else:
        print(8)
        await message.answer(get_text('false-id-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # false-id-msg

    await state.finish()


"""  HIDE  """
class HideCard(StatesGroup):
    HIDE = State()


# /hide 
async def hide_card(callback_query : CallbackQuery, state:FSMContext):
    await HideCard.HIDE.set()
    user_id = callback_query.from_user.id

    await bot.send_message(user_id, get_text('hide-card-which-one-msg', user_id)) #hide-card-which-one-msg

    bio = BytesIO()
    
    flashcards = db_get_user_cards(user_id)
    await state.update_data(card_ids=[x[0] for x in flashcards])
    for line in flashcards:
        bio.write(' | '.join(map(str, line)).encode('utf-8') + b'\n')
    bio.seek(0)

    await bot.send_document(callback_query.message.chat.id, InputFile(bio, filename='flashcards.txt'))


async def hide_state(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = db_get_language(user_id)
    card_id = message.text
    data = await state.get_data()
    if card_id.isnumeric() and int(card_id) in data['card_ids']:
        db_hide_card(card_id)
        await message.answer(get_text('hide-card-is-hidden-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) #hide-card-is-hidden-msg
    else:
        await message.answer(get_text('false-id-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) #false-id-msg

    await state.finish()


"""  EDIT  """

class EditCard(StatesGroup):
    GET_ID = State()
    EDIT_FRONT = State()
    ASK_IF_EDIT_BACK = State()
    EDIT_BACK = State()
    LEARN_AGAIN = State()


async def edit_card(callback_query : CallbackQuery, state : FSMContext):
    user_id = callback_query.from_user.id
    await EditCard.GET_ID.set()
    await bot.send_message(user_id, get_text('edit-card-which-one-msg', user_id)) #edit-card-which-one-msg
    bio = BytesIO()
    print('edit_card')
    
    flashcards = db_get_user_cards(user_id)
    await state.update_data(card_ids=[x[0] for x in flashcards])
    for line in flashcards:
        bio.write(' | '.join(map(str, line)).encode('utf-8') + b'\n')
    bio.seek(0)

    await bot.send_document(callback_query.message.chat.id, InputFile(bio, filename='flashcards.txt'))


async def ask_if_edit_front(message : Message, state : FSMContext):
    print('ask if edit front')
    card_id = message.text
    user_id = message.from_user.id
    lang = db_get_language(user_id)

    data = await state.get_data()
    if card_id.isnumeric() and int(card_id) in data['card_ids']:
        await state.update_data(card_id=card_id)
        await message.answer(get_text('edit-card-edit-front-msg', user_id), reply_markup=edit_front_kb_ru if lang == 'ru' else edit_front_kb_en) # edit-card-edit-front-msg
    else:
        await message.answer(get_text('false-id-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) #false-id-msg
        await state.finish()


async def wait_for_front(callback_query : CallbackQuery, state : FSMContext):
    print('wait for front')
    await EditCard.EDIT_FRONT.set()
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, get_text('edit-card-send-front-msg', user_id)) # edit-card-send-front-msg


async def edit_front(message : Message, state : FSMContext):
    print('edit_front')
    await EditCard.ASK_IF_EDIT_BACK.set()

    user_id = message.from_user.id
    lang = db_get_language(user_id)

    data = await state.get_data()
    card_id = data['card_id']
    front_data = message.text

    db_edit_front(card_id, front_data)

    await message.answer(get_text('edit-card-front-saved-edit-back-msg', user_id), reply_markup=edit_back_kb_ru if lang == 'ru' else edit_back_kb_en) # edit-card-front-saved-edit-back-msg


async def ask_if_edit_back(callback_query : CallbackQuery, state : FSMContext):
    await EditCard.ASK_IF_EDIT_BACK.set()
    print('ask if edit back')
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await bot.send_message(user_id, get_text('edit-card-edit-back-msg', user_id), reply_markup=edit_back_kb_ru if lang == 'ru' else edit_back_kb_en) # edit-card-edit-back-msg


async def wait_for_back(callback_query : CallbackQuery, state : FSMContext):
    print('wait for back')
    await EditCard.EDIT_BACK.set()
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, get_text('edit-card-send-back-msg', user_id)) # edit-card-send-back-msg


async def edit_back(message : Message, state : FSMContext):
    print('edit back')
    await EditCard.LEARN_AGAIN.set()
    user_id = message.from_user.id
    lang = db_get_language(user_id)
    data = await state.get_data()
    card_id = data['card_id']
    back_data = message.text
    db_edit_back(card_id, back_data)

    await message.answer(get_text('edit-card-back-saved-learn-again-msg', user_id), reply_markup=learn_again_kb_ru if lang == 'ru' else learn_again_kb_en) # edit-card-backsaved-learn-again-msg
    print('ask1')

async def ask_if_learn_again(callback_query : CallbackQuery, state : FSMContext):
    await EditCard.LEARN_AGAIN.set()
    print(0)
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await bot.send_message(user_id, get_text('edit-card-learn-again-msg', user_id), reply_markup=learn_again_kb_ru if lang == 'ru' else learn_again_kb_en) # edit-card-learn-again-msg


async def learn_again(callback_query : CallbackQuery, state : FSMContext):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    data = await state.get_data()
    card_id = data['card_id']
    if callback_query.data == 'yes_again':
        db_learn_again(card_id)
    
    await state.finish()
    await bot.send_message(user_id, get_text('edit-card-saved-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # edit-card-saved-msg


"""  REPETITION  """

class ShowCard(StatesGroup):
    NEXT = State()
    FLIP = State()


# /begin_repetition
async def begin_repetition(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    card = db_get_today_card(user_id)

    if card is None:
        await bot.send_message(user_id, get_text('no-cards-for-today-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # no-cards-for-today-msg
        return
    
    await bot.send_message(user_id, get_text('begin-review-msg', user_id), reply_markup=next_kb_ru if lang == 'ru' else next_kb_en) # begin-review-msg
    await state.set_state(ShowCard.NEXT)
    await state.update_data(card_id = card[0])
    await state.update_data(front=card[1])
    await state.update_data(back=card[2])


# /next
async def show_front(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    await state.set_state(ShowCard.FLIP)
    data = await state.get_data()
    await bot.send_message(user_id, data["front"], reply_markup=flip_kb_ru if lang == 'ru' else flip_kb_en)


# /flip
async def show_back(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    lang = db_get_language(user_id)
    data = await state.get_data()
    await bot.send_message(user_id, data["back"])
    card_id = data['card_id']
    db_update_card(card_id)
    
    card = db_get_today_card(user_id)

    if card is None:
        await bot.send_message(user_id, get_text('all-for-today-msg', user_id), reply_markup=base_kb_ru if lang == 'ru' else base_kb_en) # all-for-today-msg
        await state.finish()
        return
    
    await bot.send_message(user_id, get_text('show-next-msg', user_id), reply_markup=next_kb_ru if lang == 'ru' else next_kb_en) # show-next-msg
    await state.set_state(ShowCard.NEXT)
    await state.update_data(card_id = card[0])
    await state.update_data(front=card[1])
    await state.update_data(back=card[2])

