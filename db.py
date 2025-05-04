import sqlite3
from datetime import date, timedelta, datetime

#this file contains all the operations with the database

# data base init
conn = sqlite3.connect('flashcards.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS flashcards 
                  (card_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  user_id INTEGER, 
                  front TEXT, 
                  back TEXT, 
                  repeat_date TEXT,
                  iter INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users
			   (user_id INTEGER PRIMARY KEY,
			   language INTEGER)''')

conn.commit()

F = '%d/%m/%Y' # date format

# language = 1 --> russian
# language = 0 --> english
def db_set_language(user_id, language):
	cursor.execute('INSERT INTO users (user_id, language) VALUES (?, ?)', (user_id, language))
	conn.commit()


def db_change_language(user_id):
	cursor.execute('UPDATE users SET language = ABS(language - 1) WHERE user_id = ?', (user_id, ))
	conn.commit()


def db_get_language(user_id):
	cursor.execute('SELECT language FROM users WHERE user_id = ?', (user_id, ))
	language = cursor.fetchone()
	return 'ru' if language[0] == 1 else 'en'

def db_add_card(user_id, front, back):
	repeat_date = date.today() + timedelta(days=1)
	iter = 1 # sets the initial number of repetitions 
	cursor.execute('INSERT INTO flashcards (user_id, front, back, repeat_date, iter) VALUES (?, ?, ?, ?, ?)', (user_id, front, back, repeat_date.strftime(F), iter))
	conn.commit()


# updates repeatition date 
def db_update_card(card_id):
	cursor.execute('SELECT repeat_date, iter FROM flashcards WHERE card_id = ?', (card_id, ))
	repeat_date, iter = cursor.fetchone()
	# calculating the new repetition date
	repeat_date = datetime.strptime(repeat_date, F).date() + timedelta(days=(2**iter))
	iter += 1
	cursor.execute('UPDATE flashcards SET iter = ?, repeat_date = ? WHERE card_id = ?', (iter, repeat_date.strftime(F), card_id))
	conn.commit()


# getting all the cards to repeat today for current user
def db_get_today_cards(user_id):
	today = date.today()
	cursor.execute("SELECT card_id, front, back FROM flashcards WHERE user_id = ? AND repeat_date = ?", (user_id, today.strftime(F)))
	return cursor.fetchall()

# get one of the cards, that need to be shown today
def db_get_today_card(user_id):
	today = date.today()
	cursor.execute("SELECT card_id, front, back FROM flashcards WHERE user_id = ? AND repeat_date = ?", (user_id, today.strftime(F)))
	return cursor.fetchone()


# rescheduling all of the cards, that were supposed to be reviewed today
# happens daily for all users at 23:59
def db_reschedule_cards():
	today = date.today()
	tomorrow = today + timedelta(days=1)
	cursor.execute('UPDATE flashcards SET repeat_date = ? WHERE repeat_date = ?', (tomorrow.strftime(F), today.strftime(F)))
	conn.commit()


# getting all the users cards as a txt document
def db_get_user_cards(user_id):
	cursor.execute("SELECT card_id, front, back, repeat_date FROM flashcards WHERE user_id = ?", (user_id, ))
	return cursor.fetchall()


def db_delete_card(card_id):
	cursor.execute("DELETE FROM flashcards WHERE card_id = (?)", (card_id, ))
	conn.commit()


def db_hide_card(card_id):
	cursor.execute("UPDATE flashcards SET repeat_date = ? WHERE card_id = ?", ('0/0/0', card_id))
	conn.commit()


def db_edit_front(card_id, data):
	cursor.execute("UPDATE flashcards SET front = ? WHERE card_id = ?", (data, card_id))
	conn.commit()


def db_edit_back(card_id, data):
	cursor.execute("UPDATE flashcards SET back = ? WHERE card_id = ?", (data, card_id))
	conn.commit()


def db_learn_again(card_id):
	tomorrow = date.today() + timedelta(days=1)
	cursor.execute("UPDATE flashcards SET iter = ?, repeat_date = ? WHERE card_id = ?", (2, tomorrow.strftime(F), card_id))
	conn.commit()


def db_reschedule_cards():
	today = date.today().strftime(F)
	tomorrow = (date.today() + timedelta(days=1)).strftime(F)
	cursor.execute("UPDATE flashcards SET repeat_date = ? WHERE repeat_date = ?", (tomorrow, today))
	conn.commit()
