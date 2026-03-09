from aiogram.dispatcher.filters.state import State, StatesGroup


class SetLanguage(StatesGroup):
    GET_LANGUAGE = State()


class ChangeLanguage(StatesGroup):
    GET_CONFIRMATION = State()


class AddCard(StatesGroup):
    ADD_FRONT = State()
    ADD_BACK = State()


class DeleteCard(StatesGroup):
    GET_ID = State()


class HideCard(StatesGroup):
    HIDE = State()



class EditCard(StatesGroup):
    GET_ID = State()
    EDIT_FRONT = State()
    ASK_IF_EDIT_BACK = State()
    EDIT_BACK = State()
    LEARN_AGAIN = State()



class ShowCard(StatesGroup):
    NEXT = State()
    FLIP = State()
