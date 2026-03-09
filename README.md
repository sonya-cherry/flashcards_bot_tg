# Flashcards Telegram Bot
A Telegram bot for learning with flashcards and spaced repetition.
The bot allows users to create flashcards, review them regularly, and receive reminders to study.

---

## Features
**Add flashcards**
- Create cards with a front side (question) and back side (answer)

**Spaced repetition**
- Cards appear again after increasing intervals

**Daily review**
- See cards that are scheduled for today

**Card management**
- Edit cards
- Delete cards
- Hide cards from repetition

**Export**
- Download all flashcards as a formatted study deck

**Reminders**
- Enable daily reminders
- Choose the hour when the bot sends a notification

**Localization**
- English
- Russian

---

## Project structure
flashcards_bot_tg
│
├── app
│   ├── bot.py
│   ├── handlers.py
│   ├── keyboards.py
│   ├── states.py
│   └── texts.py
│
├── db
│   └── db.py
│
├── locales
│   ├── en.json
│   └── ru.json
│
├── main.py
├── requirements.txt

